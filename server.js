/**
 * NetSphere Pro server: static assets + authenticated JSON API.
 *
 * Storage: SQLite (node:sqlite), one JSON state document plus users,
 * sessions, backups, password-reset tokens and an email/SMS outbox.
 * Passwords use scrypt with a per-user salt. Sessions are opaque random
 * tokens stored in httpOnly cookies.
 *
 * Zero runtime dependencies (Node >= 22.5, built with Node 24).
 */
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { DatabaseSync } from "node:sqlite";

import { APP_NAME, APP_VERSION, DEMO_ACCOUNTS } from "./js/config.js";
import { createSeedData } from "./js/seed.js";

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const DATA_DIR = path.join(ROOT, "data");
const DB_FILE = process.env.NETSPHERE_DB || path.join(DATA_DIR, "netsphere.db");
const PORT = Number(process.env.PORT) || 5173;
const MAX_BODY = 12 * 1024 * 1024;
const SESSION_HOURS = 12;
const REMEMBER_DAYS = 30;
const IS_DEMO = process.env.NETSPHERE_DEMO !== "0";

fs.mkdirSync(DATA_DIR, { recursive: true });

const db = new DatabaseSync(DB_FILE);
db.exec(`
    PRAGMA journal_mode = WAL;
    PRAGMA foreign_keys = ON;
    PRAGMA busy_timeout = 5000;

    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE COLLATE NOCASE,
        name TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'admin',
        customer_id INTEGER,
        password TEXT NOT NULL,
        totp_secret TEXT,
        totp_enabled INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL,
        last_login_at TEXT
    );

    CREATE TABLE IF NOT EXISTS sessions (
        token TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        remember INTEGER NOT NULL DEFAULT 0,
        ip TEXT,
        user_agent TEXT,
        created_at INTEGER NOT NULL,
        expires_at INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS app_state (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        json TEXT NOT NULL,
        revision INTEGER NOT NULL DEFAULT 1,
        updated_at TEXT NOT NULL,
        updated_by TEXT
    );

    CREATE TABLE IF NOT EXISTS backups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT NOT NULL,
        trigger TEXT NOT NULL DEFAULT 'manual',
        created_at TEXT NOT NULL,
        created_by TEXT,
        bytes INTEGER NOT NULL,
        json TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS reset_tokens (
        token TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        expires_at INTEGER NOT NULL,
        used INTEGER NOT NULL DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS outbox (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel TEXT NOT NULL,
        recipient TEXT NOT NULL,
        subject TEXT,
        body TEXT,
        status TEXT NOT NULL DEFAULT 'simulated',
        created_at TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS audit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        at TEXT NOT NULL,
        username TEXT,
        action TEXT NOT NULL,
        details TEXT,
        ip TEXT
    );
`);

/* ------------------------------------------------------------------ */
/* Password + TOTP helpers                                             */
/* ------------------------------------------------------------------ */
function hashPassword(password) {
    const salt = crypto.randomBytes(16).toString("hex");
    const hash = crypto.scryptSync(String(password), salt, 64).toString("hex");
    return `scrypt$${salt}$${hash}`;
}

function verifyPassword(password, stored) {
    try {
        const [scheme, salt, expected] = String(stored || "").split("$");
        if (scheme !== "scrypt" || !salt || !expected) return false;
        const actual = crypto.scryptSync(String(password), salt, 64);
        const wanted = Buffer.from(expected, "hex");
        return actual.length === wanted.length && crypto.timingSafeEqual(actual, wanted);
    } catch {
        return false;
    }
}

const B32 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
function base32Encode(buffer) {
    let bits = 0;
    let value = 0;
    let output = "";
    for (const byte of buffer) {
        value = (value << 8) | byte;
        bits += 8;
        while (bits >= 5) {
            output += B32[(value >>> (bits - 5)) & 31];
            bits -= 5;
        }
    }
    if (bits > 0) output += B32[(value << (5 - bits)) & 31];
    return output;
}

function base32Decode(input) {
    let bits = 0;
    let value = 0;
    const bytes = [];
    for (const char of String(input).toUpperCase().replace(/[^A-Z2-7]/g, "")) {
        const index = B32.indexOf(char);
        if (index < 0) continue;
        value = (value << 5) | index;
        bits += 5;
        if (bits >= 8) {
            bytes.push((value >>> (bits - 8)) & 255);
            bits -= 8;
        }
    }
    return Buffer.from(bytes);
}

function totpCode(secret, offset = 0) {
    const key = base32Decode(secret);
    const counter = Math.floor(Date.now() / 1000 / 30) + offset;
    const buffer = Buffer.alloc(8);
    buffer.writeUInt32BE(Math.floor(counter / 0x100000000), 0);
    buffer.writeUInt32BE(counter >>> 0, 4);
    const digest = crypto.createHmac("sha1", key).update(buffer).digest();
    const index = digest[digest.length - 1] & 0x0f;
    const number = digest.readUInt32BE(index) & 0x7fffffff;
    return String(number % 1000000).padStart(6, "0");
}

function verifyTotp(secret, code) {
    const clean = String(code || "").replace(/\s/g, "");
    if (!/^\d{6}$/.test(clean)) return false;
    return [-1, 0, 1].some((offset) => totpCode(secret, offset) === clean);
}

/* ------------------------------------------------------------------ */
/* Session + request helpers                                           */
/* ------------------------------------------------------------------ */
const nowIso = () => new Date().toISOString();
const DAY_MS = 24 * 60 * 60 * 1000;

function parseCookies(req) {
    const result = {};
    for (const part of String(req.headers.cookie || "").split(";")) {
        const index = part.indexOf("=");
        if (index < 0) continue;
        result[part.slice(0, index).trim()] = decodeURIComponent(part.slice(index + 1).trim());
    }
    return result;
}

function sessionToken(req) {
    return parseCookies(req).ns_session || null;
}

function currentSession(req) {
    const token = sessionToken(req);
    if (!token) return null;
    const row = db
        .prepare("SELECT s.*, u.username, u.name, u.role, u.customer_id FROM sessions s JOIN users u ON u.id = s.user_id WHERE s.token = ?")
        .get(token);
    if (!row) return null;
    if (row.expires_at < Date.now()) {
        db.prepare("DELETE FROM sessions WHERE token = ?").run(token);
        return null;
    }
    return row;
}

function publicUser(row) {
    return {
        userId: row.user_id ?? row.id,
        username: row.username,
        role: row.role,
        name: row.name,
        customerId: row.customer_id ?? null,
        totpEnabled: Boolean(row.totp_enabled),
    };
}

function setCookie(res, token, remember) {
    const maxAge = remember ? REMEMBER_DAYS * 24 * 60 * 60 : SESSION_HOURS * 60 * 60;
    res.setHeader(
        "Set-Cookie",
        `ns_session=${encodeURIComponent(token)}; Path=/; HttpOnly; SameSite=Lax; Max-Age=${maxAge}`,
    );
}

function clearCookie(res) {
    res.setHeader("Set-Cookie", "ns_session=; Path=/; HttpOnly; SameSite=Lax; Max-Age=0");
}

function send(res, status, payload, headers = {}) {
    const body = typeof payload === "string" ? payload : JSON.stringify(payload);
    res.writeHead(status, {
        "Content-Type": typeof payload === "string" ? "text/plain; charset=utf-8" : "application/json; charset=utf-8",
        "Cache-Control": "no-store",
        "X-Content-Type-Options": "nosniff",
        ...headers,
    });
    res.end(body);
}

function readBody(req) {
    return new Promise((resolve, reject) => {
        let size = 0;
        const chunks = [];
        req.on("data", (chunk) => {
            size += chunk.length;
            if (size > MAX_BODY) {
                reject(Object.assign(new Error("Request body too large."), { status: 413 }));
                req.destroy();
                return;
            }
            chunks.push(chunk);
        });
        req.on("end", () => {
            if (!chunks.length) return resolve({});
            try {
                const parsed = JSON.parse(Buffer.concat(chunks).toString("utf8"));
                resolve(parsed && typeof parsed === "object" ? parsed : {});
            } catch {
                reject(Object.assign(new Error("Invalid JSON body."), { status: 400 }));
            }
        });
        req.on("error", reject);
    });
}

function audit(req, username, action, details = "") {
    try {
        db.prepare("INSERT INTO audit (at, username, action, details, ip) VALUES (?, ?, ?, ?, ?)").run(
            nowIso(),
            username || null,
            action,
            String(details || "").slice(0, 1000),
            req.socket.remoteAddress || null,
        );
    } catch (error) {
        console.warn("[audit]", error.message);
    }
}

function outbox(channel, recipient, subject, body) {
    db.prepare("INSERT INTO outbox (channel, recipient, subject, body, status, created_at) VALUES (?, ?, ?, ?, 'simulated', ?)").run(
        channel,
        recipient || "unset",
        subject || null,
        body || null,
        nowIso(),
    );
}

/* ------------------------------------------------------------------ */
/* Rate limiting                                                       */
/* ------------------------------------------------------------------ */
const attempts = new Map();
function rateLimit(req, key, limit = 8, windowMs = 15 * 60 * 1000) {
    const identity = `${req.socket.remoteAddress || "local"}:${key}`;
    const now = Date.now();
    const entry = attempts.get(identity);
    if (!entry || entry.reset < now) {
        attempts.set(identity, { count: 1, reset: now + windowMs });
        return true;
    }
    entry.count += 1;
    if (entry.count > limit) return false;
    return true;
}
function clearRateLimit(req, key) {
    attempts.delete(`${req.socket.remoteAddress || "local"}:${key}`);
}

/* ------------------------------------------------------------------ */
/* State storage                                                       */
/* ------------------------------------------------------------------ */
function sanitiseStateForClient(state) {
    return {
        ...state,
        users: (state.users || []).map((user) => ({
            id: user.id,
            username: user.username,
            role: user.role,
            name: user.name,
            customerId: user.customerId ?? null,
            lastLoginAt: user.lastLoginAt || null,
        })),
    };
}

function readState() {
    const row = db.prepare("SELECT json, revision FROM app_state WHERE id = 1").get();
    return { state: JSON.parse(row.json), revision: row.revision };
}

function writeState(state, username, req, { createBackup = false } = {}) {
    const current = db.prepare("SELECT revision FROM app_state WHERE id = 1").get();
    const revision = (current?.revision || 0) + 1;
    const json = JSON.stringify(state);
    db.prepare("UPDATE app_state SET json = ?, revision = ?, updated_at = ?, updated_by = ? WHERE id = 1").run(
        json,
        revision,
        nowIso(),
        username || null,
    );
    if (createBackup) createDbBackup(`Auto backup - revision ${revision}`, "auto", username);
    audit(req, username, "State Saved", `revision ${revision}`);
    return revision;
}

function createDbBackup(label, trigger = "manual", username = "system") {
    const { state } = readState();
    const json = JSON.stringify(state);
    const result = db
        .prepare("INSERT INTO backups (label, trigger, created_at, created_by, bytes, json) VALUES (?, ?, ?, ?, ?, ?)")
        .run(String(label || "Manual backup").slice(0, 120), trigger, nowIso(), username || "system", Buffer.byteLength(json), json);
    return Number(result.lastInsertRowid);
}

function seedDatabase() {
    let state = createSeedData();
    const existing = db.prepare("SELECT COUNT(*) AS count FROM app_state").get();
    if (!existing.count) {
        db.prepare("INSERT INTO app_state (id, json, revision, updated_at, updated_by) VALUES (1, ?, 1, ?, ?)").run(
            JSON.stringify(state),
            nowIso(),
            "system",
        );
    } else {
        state = readState().state;
    }

    const insert = db.prepare(
        "INSERT INTO users (username, name, role, customer_id, password, created_at) VALUES (?, ?, ?, ?, ?, ?)",
    );
    for (const account of Object.values(DEMO_ACCOUNTS)) {
        const exists = db.prepare("SELECT id FROM users WHERE username = ?").get(account.username);
        if (exists) continue;
        const linked = state.users?.find((user) => user.username === account.username);
        insert.run(
            account.username,
            account.name || account.username,
            account.role,
            linked?.customerId ?? (account.role === "customer" ? state.customers[0]?.id ?? null : null),
            hashPassword(account.password),
            nowIso(),
        );
    }
    // Keep the account model to the two supported roles: administrator and customer.
    if (IS_DEMO) {
        db.prepare("DELETE FROM users WHERE role NOT IN ('admin', 'customer')").run();
        db.prepare("DELETE FROM sessions WHERE user_id NOT IN (SELECT id FROM users)").run();
    }
}
seedDatabase();

/* ------------------------------------------------------------------ */
/* Customer write authorisation                                        */
/* ------------------------------------------------------------------ */
function sanitiseCustomerState(oldState, incoming, session) {
    const next = JSON.parse(JSON.stringify(incoming));
    const old = oldState;
    const customerId = session.customer_id;

    next.users = old.users;
    next.packages = old.packages;
    next.staff = old.staff;
    next.devices = old.devices;
    next.ipPool = old.ipPool;
    next.outages = old.outages;
    next.bandwidthLogs = old.bandwidthLogs;
    next.nodeBandwidth = old.nodeBandwidth;
    next.sequences = old.sequences;
    const oldSettings = old.settings || {};
    next.settings = { ...oldSettings };
    if (incoming.settings?.theme === "light" || incoming.settings?.theme === "dark") {
        next.settings.theme = incoming.settings.theme;
    }

    next.customers = (old.customers || []).map((customer) => {
        if (customer.id !== customerId) return customer;
        const proposed = (incoming.customers || []).find((entry) => entry.id === customerId) || {};
        return {
            ...customer,
            name: typeof proposed.name === "string" && proposed.name.trim() ? proposed.name.trim().slice(0, 80) : customer.name,
            phone: typeof proposed.phone === "string" ? proposed.phone.slice(0, 40) : customer.phone,
            address: typeof proposed.address === "string" ? proposed.address.slice(0, 160) : customer.address,
            notificationPrefs: proposed.notificationPrefs && typeof proposed.notificationPrefs === "object"
                ? {
                      email: proposed.notificationPrefs.email !== false,
                      sms: Boolean(proposed.notificationPrefs.sms),
                      invoices: proposed.notificationPrefs.invoices !== false,
                      outages: proposed.notificationPrefs.outages !== false,
                      tickets: proposed.notificationPrefs.tickets !== false,
                  }
                : customer.notificationPrefs,
        };
    });

    next.invoices = (old.invoices || []).map((invoice) => {
        if (invoice.customerId !== customerId) return invoice;
        const proposed = (incoming.invoices || []).find((entry) => entry.id === invoice.id);
        if (!proposed) return invoice;
        const paid = Number(proposed.amountPaid);
        const amountPaid = Number.isFinite(paid) ? Math.max(0, Math.min(invoice.amount, paid)) : invoice.amountPaid || 0;
        return {
            ...invoice,
            amountPaid,
            status: amountPaid >= invoice.amount ? "paid" : amountPaid > 0 ? "partial" : invoice.status === "paid" ? "unpaid" : invoice.status,
            paidAt: amountPaid >= invoice.amount ? proposed.paidAt || invoice.paidAt : null,
            method: proposed.method || invoice.method,
            payments: Array.isArray(proposed.payments)
                ? proposed.payments.map((payment) => ({
                      id: String(payment.id || crypto.randomUUID()),
                      amount: Number(payment.amount) || 0,
                      method: String(payment.method || "online").slice(0, 40),
                      reference: String(payment.reference || "").slice(0, 80),
                      at: payment.at || nowIso(),
                      gateway: String(payment.gateway || "sandbox").slice(0, 40),
                  }))
                : invoice.payments || [],
        };
    });

    const oldTickets = new Map((old.tickets || []).map((ticket) => [ticket.id, ticket]));
    next.tickets = (incoming.tickets || [])
        .filter((ticket) => ticket.customerId === customerId)
        .map((ticket) => {
            const existing = oldTickets.get(ticket.id);
            if (!existing) {
                return {
                    ...ticket,
                    customerId,
                    status: "open",
                    assignedTo: null,
                    comments: [],
                    history: [{ at: nowIso(), by: session.username, action: "Created" }],
                };
            }
            return {
                ...existing,
                status: ["open", "in-progress", "closed"].includes(ticket.status) ? ticket.status : existing.status,
                comments: Array.isArray(ticket.comments)
                    ? ticket.comments.map((comment) => ({
                          id: String(comment.id || crypto.randomUUID()),
                          author: String(comment.author || session.username).slice(0, 60),
                          role: "customer",
                          text: String(comment.text || "").slice(0, 4000),
                          at: comment.at || nowIso(),
                          attachments: Array.isArray(comment.attachments) ? comment.attachments.slice(0, 3) : [],
                      }))
                    : existing.comments || [],
                updatedAt: nowIso().slice(0, 10),
            };
        });
    const existingTicketIds = new Set(next.tickets.map((ticket) => ticket.id));
    for (const ticket of old.tickets || []) {
        if (ticket.customerId !== customerId) {
            next.tickets.push(ticket);
        } else if (!existingTicketIds.has(ticket.id)) {
            next.tickets.push(ticket);
        }
    }

    next.activityLogs = Array.isArray(old.activityLogs) ? old.activityLogs : [];
    return next;
}

/* ------------------------------------------------------------------ */
/* API routes                                                          */
/* ------------------------------------------------------------------ */
const routes = [];
const route = (method, pattern, handler, options = {}) => routes.push({ method, pattern, handler, options });

async function handleApi(req, res, url) {
    const pathname = url.pathname;
    const match = routes.find((entry) => {
        if (entry.method !== req.method) return false;
        const names = [];
        const regex = new RegExp(`^${entry.pattern.replace(/:([a-zA-Z]+)/g, (_, name) => {
            names.push(name);
            return "([^/]+)";
        })}$`);
        const result = regex.exec(pathname);
        if (!result) return false;
        return { params: Object.fromEntries(names.map((name, index) => [name, decodeURIComponent(result[index + 1])])) };
    });
    if (!match) return send(res, 404, { error: "Unknown API endpoint." });

    const regex = new RegExp(`^${match.pattern.replace(/:([a-zA-Z]+)/g, () => "([^/]+)")}$`);
    const result = regex.exec(pathname);
    const names = [...match.pattern.matchAll(/:([a-zA-Z]+)/g)].map((entry) => entry[1]);
    const params = Object.fromEntries(names.map((name, index) => [name, decodeURIComponent(result[index + 1])]));

    const session = currentSession(req);
    if (!match.options.public && !session) return send(res, 401, { error: "Please sign in to continue." });
    if (match.options.admin && session?.role !== "admin") return send(res, 403, { error: "Administrator access required." });

    try {
        const body = ["POST", "PUT", "PATCH", "DELETE"].includes(req.method) ? await readBody(req) : {};
        return await match.handler({ req, res, url, body, params, session });
    } catch (error) {
        console.error("[api]", error);
        return send(res, error.status || 500, { error: error.message || "Server error." });
    }
}

/* Health & session -------------------------------------------------- */
route("GET", "/api/health", ({ res }) => {
    send(res, 200, { ok: true, app: APP_NAME, version: APP_VERSION, database: "sqlite", demo: IS_DEMO, time: nowIso() });
}, { public: true });

route("GET", "/api/auth/session", ({ res, session }) => {
    if (!session) return send(res, 200, { authenticated: false, demo: IS_DEMO });
    const user = db.prepare("SELECT * FROM users WHERE id = ?").get(session.user_id);
    const { state, revision } = readState();
    send(res, 200, {
        authenticated: true,
        user: { ...publicUser({ ...user, user_id: user.id }), totpEnabled: Boolean(user.totp_enabled) },
        state: sanitiseStateForClient(state),
        revision,
    });
}, { public: true });

route("POST", "/api/auth/login", ({ req, res, body }) => {
    if (!rateLimit(req, "login")) return send(res, 429, { error: "Too many sign-in attempts. Try again in 15 minutes." });
    const username = String(body.username || "").trim();
    const password = String(body.password || "");
    if (!username || !password) return send(res, 400, { error: "Username and password are required." });

    const user = db.prepare("SELECT * FROM users WHERE username = ? COLLATE NOCASE").get(username);
    if (!user || !verifyPassword(password, user.password)) {
        audit(req, username, "Login Failed", "Invalid credentials");
        return send(res, 401, { error: "Invalid username or password." });
    }
    if (body.role && user.role !== body.role) {
        return send(res, 401, { error: `This account is registered as ${user.role}. Select "${user.role}" to sign in.` });
    }

    if (user.totp_enabled) {
        if (!body.totp) return send(res, 202, { totpRequired: true, error: "Enter your authenticator code." });
        if (!verifyTotp(user.totp_secret, body.totp)) {
            return send(res, 401, { error: "Invalid authenticator code." });
        }
    }

    clearRateLimit(req, "login");
    const remember = Boolean(body.remember);
    const token = crypto.randomBytes(32).toString("hex");
    const expiresAt = Date.now() + (remember ? REMEMBER_DAYS : SESSION_HOURS) * 60 * 60 * 1000;
    db.prepare("INSERT INTO sessions (token, user_id, remember, ip, user_agent, created_at, expires_at) VALUES (?, ?, ?, ?, ?, ?, ?)").run(
        token,
        user.id,
        remember ? 1 : 0,
        req.socket.remoteAddress || null,
        String(req.headers["user-agent"] || "").slice(0, 300),
        Date.now(),
        expiresAt,
    );
    db.prepare("UPDATE users SET last_login_at = ? WHERE id = ?").run(nowIso(), user.id);
    setCookie(res, token, remember);
    audit(req, user.username, "Signed In", `${user.role} session`);

    const { state, revision } = readState();
    send(res, 200, {
        authenticated: true,
        user: { ...publicUser({ ...user, user_id: user.id }), totpEnabled: Boolean(user.totp_enabled) },
        state: sanitiseStateForClient(state),
        revision,
    });
}, { public: true });

route("POST", "/api/auth/logout", ({ req, res, session }) => {
    if (session) {
        db.prepare("DELETE FROM sessions WHERE token = ?").run(session.token);
        audit(req, session.username, "Signed Out", `${session.role} session`);
    }
    clearCookie(res);
    send(res, 200, { ok: true });
}, { public: true });

route("POST", "/api/auth/register", ({ req, res, body }) => {
    if (!rateLimit(req, "register", 5, 60 * 60 * 1000)) return send(res, 429, { error: "Too many registration attempts." });
    const name = String(body.name || "").trim();
    const email = String(body.email || "").trim().toLowerCase();
    const password = String(body.password || "");
    const packageId = Number(body.packageId) || 1;
    if (!name || !email || !password) return send(res, 400, { error: "All fields are required." });
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return send(res, 400, { error: "Enter a valid email address." });
    if (password.length < 8) return send(res, 400, { error: "Password must be at least 8 characters." });
    if (db.prepare("SELECT id FROM users WHERE username = ? COLLATE NOCASE").get(email)) {
        return send(res, 409, { error: "An account with this email already exists." });
    }

    const { state } = readState();
    if (state.customers.some((customer) => String(customer.email).toLowerCase() === email)) {
        return send(res, 409, { error: "An account with this email already exists." });
    }
    const customerId = Number(state.sequences.customer) || state.customers.length + 1;
    state.sequences.customer = customerId + 1;
    const pkg = state.packages.find((entry) => entry.id === packageId) || state.packages[0];
    state.customers.push({
        id: customerId,
        name,
        email,
        phone: "",
        packageId: pkg?.id || 1,
        status: "active",
        connection: "offline",
        dataUsed: 0,
        lat: 27.7172,
        lng: 85.324,
        address: "Kathmandu",
        node: "KTM-Central",
        ip: "",
        joinedAt: nowIso().slice(0, 10),
        billingDay: new Date().getDate(),
        notes: "Self-registered via portal",
        notificationPrefs: { email: true, sms: false, invoices: true, outages: true, tickets: true },
    });
    state.sequences.user = Number(state.sequences.user || 3);
    state.users = state.users || [];
    state.users.push({
        id: state.sequences.user,
        username: email,
        role: "customer",
        name,
        customerId,
        lastLoginAt: nowIso(),
    });
    state.sequences.user += 1;

    const result = db.prepare("INSERT INTO users (username, name, role, customer_id, password, created_at) VALUES (?, ?, 'customer', ?, ?, ?)").run(
        email,
        name,
        customerId,
        hashPassword(password),
        nowIso(),
    );
    writeState(state, email, req);
    audit(req, email, "Registered", `Customer #${customerId}`);
    outbox("email", email, "Welcome to NetSphere Pro", `Hello ${name}, your customer portal account is ready.`);

    const user = db.prepare("SELECT * FROM users WHERE id = ?").get(Number(result.lastInsertRowid));
    const token = crypto.randomBytes(32).toString("hex");
    db.prepare("INSERT INTO sessions (token, user_id, remember, ip, user_agent, created_at, expires_at) VALUES (?, ?, 0, ?, ?, ?, ?)").run(
        token,
        user.id,
        req.socket.remoteAddress || null,
        String(req.headers["user-agent"] || "").slice(0, 300),
        Date.now(),
        Date.now() + SESSION_HOURS * 60 * 60 * 1000,
    );
    setCookie(res, token, false);
    const latest = readState();
    send(res, 201, {
        authenticated: true,
        user: { ...publicUser({ ...user, user_id: user.id }), totpEnabled: false },
        state: sanitiseStateForClient(latest.state),
        revision: latest.revision,
    });
}, { public: true });

route("POST", "/api/auth/forgot", ({ req, res, body }) => {
    if (!rateLimit(req, "forgot", 5, 15 * 60 * 1000)) return send(res, 429, { error: "Too many reset requests." });
    const username = String(body.username || "").trim();
    const user = db.prepare("SELECT * FROM users WHERE username = ? COLLATE NOCASE").get(username);
    const token = crypto.randomBytes(24).toString("hex");
    if (user) {
        db.prepare("INSERT INTO reset_tokens (token, user_id, expires_at, used) VALUES (?, ?, ?, 0)").run(
            token,
            user.id,
            Date.now() + 30 * 60 * 1000,
        );
        outbox("email", user.username, "Reset your NetSphere password", `Reset token: ${token} (expires in 30 minutes)`);
        audit(req, username, "Password Reset Requested", "Token generated");
    }
    send(res, 200, {
        ok: true,
        message: "If that account exists, reset instructions have been sent.",
        demoToken: IS_DEMO && user ? token : undefined,
    });
}, { public: true });

route("POST", "/api/auth/reset", ({ req, res, body }) => {
    const token = String(body.token || "");
    const password = String(body.password || "");
    if (password.length < 8) return send(res, 400, { error: "Password must be at least 8 characters." });
    const row = db.prepare("SELECT * FROM reset_tokens WHERE token = ? AND used = 0").get(token);
    if (!row || row.expires_at < Date.now()) return send(res, 400, { error: "Reset token is invalid or expired." });
    db.prepare("UPDATE users SET password = ? WHERE id = ?").run(hashPassword(password), row.user_id);
    db.prepare("UPDATE reset_tokens SET used = 1 WHERE token = ?").run(token);
    db.prepare("DELETE FROM sessions WHERE user_id = ?").run(row.user_id);
    audit(req, null, "Password Reset", `User #${row.user_id}`);
    send(res, 200, { ok: true });
}, { public: true });

route("POST", "/api/auth/password", ({ req, res, body, session }) => {
    const user = db.prepare("SELECT * FROM users WHERE id = ?").get(session.user_id);
    if (!verifyPassword(String(body.current || ""), user.password)) {
        return send(res, 400, { error: "Current password is incorrect." });
    }
    if (String(body.next || "").length < 8) return send(res, 400, { error: "New password must be at least 8 characters." });
    db.prepare("UPDATE users SET password = ? WHERE id = ?").run(hashPassword(body.next), user.id);
    db.prepare("DELETE FROM sessions WHERE user_id = ? AND token <> ?").run(user.id, session.token);
    audit(req, user.username, "Password Changed", "");
    send(res, 200, { ok: true });
});

/* 2FA --------------------------------------------------------------- */
route("POST", "/api/auth/2fa/setup", ({ req, res, session }) => {
    const secret = base32Encode(crypto.randomBytes(20));
    db.prepare("UPDATE users SET totp_secret = ?, totp_enabled = 0 WHERE id = ?").run(secret, session.user_id);
    const label = encodeURIComponent(`${APP_NAME}:${session.username}`);
    send(res, 200, {
        secret,
        otpauth: `otpauth://totp/${label}?secret=${secret}&issuer=${encodeURIComponent(APP_NAME)}&digits=6&period=30`,
    });
});

route("POST", "/api/auth/2fa/enable", ({ req, res, body, session }) => {
    const user = db.prepare("SELECT * FROM users WHERE id = ?").get(session.user_id);
    if (!user.totp_secret || !verifyTotp(user.totp_secret, body.code)) {
        return send(res, 400, { error: "Invalid authenticator code." });
    }
    db.prepare("UPDATE users SET totp_enabled = 1 WHERE id = ?").run(user.id);
    audit(req, user.username, "2FA Enabled", "");
    send(res, 200, { ok: true });
});

route("POST", "/api/auth/2fa/disable", ({ req, res, body, session }) => {
    const user = db.prepare("SELECT * FROM users WHERE id = ?").get(session.user_id);
    if (!verifyPassword(String(body.password || ""), user.password)) {
        return send(res, 400, { error: "Password is incorrect." });
    }
    db.prepare("UPDATE users SET totp_enabled = 0, totp_secret = NULL WHERE id = ?").run(user.id);
    audit(req, user.username, "2FA Disabled", "");
    send(res, 200, { ok: true });
});

/* State ------------------------------------------------------------- */
route("GET", "/api/state", ({ res, session }) => {
    const { state, revision } = readState();
    send(res, 200, { state: sanitiseStateForClient(state), revision, user: publicUser(session) });
});

route("PUT", "/api/state", ({ req, res, body, session }) => {
    if (!body.state || typeof body.state !== "object") return send(res, 400, { error: "Missing state payload." });
    const current = readState();
    if (body.revision && Number(body.revision) !== current.revision) {
        return send(res, 409, {
            error: "This workspace was updated in another session. Reload to continue.",
            conflict: true,
            state: sanitiseStateForClient(current.state),
            revision: current.revision,
        });
    }
    const nextState = session.role !== "customer"
        ? { ...body.state, users: current.state.users }
        : sanitiseCustomerState(current.state, body.state, session);
    if (!Array.isArray(nextState.customers) || !Array.isArray(nextState.packages)) {
        return send(res, 400, { error: "Invalid workspace state." });
    }
    const last = db.prepare("SELECT created_at FROM backups ORDER BY id DESC LIMIT 1").get();
    const shouldBackup = !last || Date.now() - new Date(last.created_at).getTime() > DAY_MS;
    const revision = writeState(nextState, session.username, req, { createBackup: shouldBackup });
    send(res, 200, { ok: true, revision, backedUp: shouldBackup });
});

/* Backups ----------------------------------------------------------- */
route("GET", "/api/backups", ({ res }) => {
    const rows = db
        .prepare("SELECT id, label, trigger, created_at, created_by, bytes FROM backups ORDER BY id DESC LIMIT 50")
        .all();
    send(res, 200, { backups: rows });
}, { admin: true });

route("POST", "/api/backups", ({ req, res, body, session }) => {
    const id = createDbBackup(body.label || `Manual backup ${nowIso().slice(0, 16).replace("T", " ")}`, "manual", session.username);
    audit(req, session.username, "Backup Created", `#${id}`);
    send(res, 201, { ok: true, id });
}, { admin: true });

route("POST", "/api/backups/:id/restore", ({ req, res, params, session }) => {
    const row = db.prepare("SELECT * FROM backups WHERE id = ?").get(Number(params.id));
    if (!row) return send(res, 404, { error: "Backup not found." });
    const parsed = JSON.parse(row.json);
    if (!Array.isArray(parsed.customers) || !Array.isArray(parsed.packages)) {
        return send(res, 400, { error: "Backup is not a valid workspace." });
    }
    writeState(parsed, session.username, req);
    audit(req, session.username, "Backup Restored", `#${row.id} ${row.label}`);
    send(res, 200, { ok: true });
}, { admin: true });

route("DELETE", "/api/backups/:id", ({ req, res, params, session }) => {
    db.prepare("DELETE FROM backups WHERE id = ?").run(Number(params.id));
    audit(req, session.username, "Backup Deleted", `#${params.id}`);
    send(res, 200, { ok: true });
}, { admin: true });

route("GET", "/api/backups/:id/download", ({ res, params }) => {
    const row = db.prepare("SELECT * FROM backups WHERE id = ?").get(Number(params.id));
    if (!row) return send(res, 404, { error: "Backup not found." });
    const filename = `netsphere-backup-${row.id}-${row.created_at.slice(0, 10)}.json`;
    res.writeHead(200, {
        "Content-Type": "application/json; charset=utf-8",
        "Content-Disposition": `attachment; filename="${filename}"`,
        "Cache-Control": "no-store",
    });
    res.end(row.json);
}, { admin: true });

/* Snapshot import/export (admin) ------------------------------------ */
route("POST", "/api/state/import", ({ req, res, body, session }) => {
    const parsed = body.state;
    if (!parsed || !Array.isArray(parsed.customers) || !Array.isArray(parsed.packages)) {
        return send(res, 400, { error: "Invalid backup file." });
    }
    const current = readState();
    parsed.users = current.state.users;
    writeState(parsed, session.username, req, { createBackup: true });
    audit(req, session.username, "State Imported", "JSON snapshot");
    send(res, 200, { ok: true });
}, { admin: true });

route("POST", "/api/state/reset", ({ req, res, session }) => {
    createDbBackup("Before demo reset", "auto", session.username);
    const fresh = createSeedData();
    writeState(fresh, session.username, req);
    audit(req, session.username, "Demo Data Reset", "");
    send(res, 200, { ok: true, state: sanitiseStateForClient(fresh), revision: readState().revision });
}, { admin: true });

/* Email/SMS outbox -------------------------------------------------- */
route("POST", "/api/notify", ({ req, res, body, session }) => {
    const channel = body.channel === "sms" ? "sms" : "email";
    outbox(channel, body.recipient, body.subject, body.body);
    audit(req, session.username, "Notification Queued", `${channel} -> ${body.recipient}`);
    send(res, 202, { ok: true, simulated: true });
});

route("GET", "/api/outbox", ({ res }) => {
    const rows = db.prepare("SELECT * FROM outbox ORDER BY id DESC LIMIT 100").all();
    send(res, 200, { messages: rows });
}, { admin: true });

/* Sessions + account audit ----------------------------------------- */
route("GET", "/api/sessions", ({ res, session }) => {
    const rows = db
        .prepare("SELECT token, ip, user_agent, created_at, expires_at FROM sessions WHERE user_id = ? ORDER BY created_at DESC")
        .all(session.user_id)
        .map((row) => ({
            current: row.token === session.token,
            ip: row.ip,
            userAgent: row.user_agent,
            createdAt: row.created_at,
            expiresAt: row.expires_at,
        }));
    send(res, 200, { sessions: rows });
});

route("DELETE", "/api/sessions", ({ req, res, session, body }) => {
    if (body.all && body.all !== session.token) {
        db.prepare("DELETE FROM sessions WHERE user_id = ? AND token <> ?").run(session.user_id, session.token);
        audit(req, session.username, "Sessions Revoked", "All other devices");
        return send(res, 200, { ok: true });
    }
    send(res, 400, { error: "Nothing to revoke." });
});

/* ------------------------------------------------------------------ */
/* Static server                                                       */
/* ------------------------------------------------------------------ */
const MIME = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".mjs": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".webmanifest": "application/manifest+json; charset=utf-8",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".ico": "image/x-icon",
    ".woff2": "font/woff2",
    ".txt": "text/plain; charset=utf-8",
};

const SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=(self)",
    "Cross-Origin-Opener-Policy": "same-origin",
    "Content-Security-Policy": [
        "default-src 'self'",
        "script-src 'self' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://unpkg.com",
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com https://unpkg.com",
        "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com data:",
        "img-src 'self' data: blob: https://tile.openstreetmap.org https://*.tile.openstreetmap.org https://unpkg.com",
        "connect-src 'self'",
        "frame-ancestors 'none'",
        "base-uri 'self'",
        "form-action 'self'",
    ].join("; "),
};

function serveStatic(req, res, url) {
    const urlPath = decodeURIComponent(url.pathname === "/" ? "/index.html" : url.pathname);
    const filePath = path.resolve(ROOT, `.${urlPath}`);
    const relative = path.relative(ROOT, filePath);
    if (relative.startsWith("..") || path.isAbsolute(relative) || relative.split(path.sep)[0] === "data") {
        res.writeHead(403, SECURITY_HEADERS).end("Forbidden");
        return;
    }
    if (!fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
        res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8", ...SECURITY_HEADERS }).end("404 Not Found");
        return;
    }
    const ext = path.extname(filePath).toLowerCase();
    const noCache = ext === ".html" || path.basename(filePath) === "sw.js";
    res.writeHead(200, {
        "Content-Type": MIME[ext] || "application/octet-stream",
        "Cache-Control": noCache ? "no-cache, max-age=0, must-revalidate" : "public, max-age=60",
        ...SECURITY_HEADERS,
    });
    fs.createReadStream(filePath).pipe(res);
}

const server = http.createServer(async (req, res) => {
    const url = new URL(req.url || "/", `http://${req.headers.host || "localhost"}`);
    if (url.pathname.startsWith("/api/")) {
        try {
            await handleApi(req, res, url);
        } catch (error) {
            console.error("[server]", error);
            if (!res.headersSent) send(res, 500, { error: "Internal server error." });
        }
        return;
    }
    if (req.method !== "GET" && req.method !== "HEAD") {
        res.writeHead(405, { Allow: "GET, HEAD", ...SECURITY_HEADERS }).end("Method Not Allowed");
        return;
    }
    serveStatic(req, res, url);
});

server.on("error", (error) => {
    if (error.code === "EADDRINUSE") {
        console.error(`\nPort ${PORT} is already in use — ${APP_NAME} may already be running.`);
        console.error(`Open http://localhost:${PORT} in your browser.`);
        console.error(`To stop the existing server:  npm run stop\n`);
        process.exit(1);
    }
    throw error;
});

server.listen(PORT, () => {
    console.log(`${APP_NAME} v${APP_VERSION} running at http://localhost:${PORT}`);
    console.log(`SQLite database: ${DB_FILE}`);
});
