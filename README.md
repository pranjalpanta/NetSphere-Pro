# NetSphere Pro

**A complete, self-hosted ISP management platform** — subscribers, packages, VAT billing,
support, network operations, analytics and a customer self-service portal, in a single
install with **zero runtime dependencies**.

![Node](https://img.shields.io/badge/node-%E2%89%A524-339933?logo=node.js&logoColor=white)
![Runtime deps](https://img.shields.io/badge/runtime%20dependencies-0-16a34a)
![Tests](https://img.shields.io/badge/tests-smoke%20%2B%20e2e-6366f1)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## Table of contents

- [Overview](#overview)
- [Highlights](#highlights)
- [Tech stack](#tech-stack)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Demo accounts](#demo-accounts)
- [npm scripts](#npm-scripts)
- [Configuration](#configuration)
- [Features](#features)
- [Roles & permissions](#roles--permissions)
- [Architecture](#architecture)
- [Data model](#data-model)
- [API reference](#api-reference)
- [Project structure](#project-structure)
- [Testing](#testing)
- [Docker](#docker)
- [Production deployment](#production-deployment)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Limitations & roadmap](#limitations--roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

NetSphere Pro is an operations platform for internet service providers (ISPs). It pairs a
**framework-free front end** with a **zero-dependency Node server** and an **embedded SQLite
database**, so a single `npm start` yields a fully working, persistent, multi-user system —
no build step, no bundler, no external services and no package installation required just to
run it.

The application ships with two access modes:

- a full **Admin** workspace for staff — billing, support, network operations and analytics;
- a focused **Customer** portal for subscribers — usage, invoices, payments and tickets.

Everything is stored server-side in SQLite and stays consistent across browsers through a
revisioned sync protocol, with a local cache that keeps the app usable offline.

## Highlights

- **Zero runtime dependencies** — the app and server use only Node's standard library:
  `node:sqlite`, `node:crypto`, `node:http`, `node:fs`, `node:path`.
- **No build step** — edit the ES modules and reload the browser; the source runs directly.
- **Real persistence and authentication** — SQLite storage, `scrypt` password hashing,
  `HttpOnly` session cookies, TOTP two-factor authentication and a full audit trail.
- **Revisioned state sync** — the client and server reconcile workspace state through a
  monotonic revision counter; concurrent edits surface a `409` conflict instead of silently
  overwriting each other.
- **Installable PWA** — an app-shell service worker, an offline fallback page and
  self-updating assets.
- **Tested and automated** — a jsdom DOM smoke suite plus a Playwright browser suite, wired
  into a CI pipeline with lint and report artifacts.
- **Portable** — runs on a laptop, in Docker, or on any Node 24+ host behind a reverse proxy.

## Tech stack

| Layer          | Choice                                                                 |
| -------------- | ---------------------------------------------------------------------- |
| Front end      | Vanilla ES modules + a hand-written CSS design system (no framework)   |
| Charts & maps  | Chart.js · Leaflet with OpenStreetMap tiles                            |
| Server         | Node.js `http` module (no framework)                                   |
| Database       | `node:sqlite` (`DatabaseSync`) in WAL mode                             |
| Security       | `scrypt` hashing, `HttpOnly` cookies, CSP + hardening headers, TOTP    |
| PWA            | Service worker, Web App Manifest, offline fallback                     |
| Testing        | jsdom (DOM smoke), Playwright (browser E2E), ESLint                    |
| Tooling        | Docker / Compose, GitHub Actions                                       |

## Requirements

| Requirement | Version      | Notes                                                       |
| ----------- | ------------ | ----------------------------------------------------------- |
| Node.js     | **24+**      | Required for the built-in `node:sqlite` module              |
| npm         | bundled      | Used only for scripts and dev tooling                       |
| Browser     | modern       | Chromium, Firefox or WebKit (Edge for local E2E runs)       |

> There are **no runtime dependencies** to install. `npm install` pulls dev tooling only
> (ESLint, Prettier, jsdom, Playwright).

## Quick start

```bash
# 1. (optional) install dev tooling for tests and linting
npm install

# 2. start the server
npm start
```

Open <http://localhost:5173>. The SQLite database is created automatically at
`data/netsphere.db` and seeded with an idempotent demo dataset on the first run.

## Demo accounts

| Role          | Username   | Password       | Lands on          |
| ------------- | ---------- | -------------- | ----------------- |
| Administrator | `admin`    | `admin123`     | Admin workspace   |
| Customer      | `customer` | `customer123`  | Customer portal   |

Pick a role on the sign-in screen — the demo credentials are prefilled for convenience.
Set `NETSPHERE_DEMO=0` to disable demo accounts in production.

## npm scripts

| Script               | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| `npm start`          | Run the server on `http://localhost:5173`                  |
| `npm run dev`        | Same as start, for local development                       |
| `npm run stop`       | Free the port by stopping the listening server process     |
| `npm run lint`       | Lint the `js/` tree with ESLint                             |
| `npm run format`     | Format sources with Prettier                                |
| `npm run test:smoke` | jsdom DOM smoke suite (requires the server on `:5173`)     |
| `npm run test:e2e`   | Playwright browser suite (auto-starts a server on `:5180`)  |
| `npm test`           | `lint` + `test:smoke` + `test:e2e`                          |

## Configuration

| Variable         | Default              | Description                                              |
| ---------------- | -------------------- | -------------------------------------------------------- |
| `PORT`           | `5173`               | Port the HTTP server listens on                           |
| `NETSPHERE_DB`   | `data/netsphere.db`  | Path to the SQLite database file                          |
| `NETSPHERE_DEMO` | `1`                  | Set to `0` to disable demo accounts and first-run seeding |

Example:

```bash
PORT=8080 NETSPHERE_DB=/var/lib/netsphere/netsphere.db NETSPHERE_DEMO=0 npm start
```

## Features

### Operations

- **Dashboard** — revenue trend, package mix, recent payments, expiring subscriptions and a
  live system snapshot.
- **Customers** — create, edit and delete records; search and filter; pagination; bulk
  actions; CSV import and export; per-customer profile with connection status, node and plan.
- **Packages** — plans with speeds, data caps and pricing; subscribers are safely reassigned
  when a package is removed.
- **Billing** — monthly invoice generation, a complete status lifecycle
  (`unpaid → partial → overdue → paid/refunded`), partial payments via cash, bank or
  simulated gateways, credit notes, refunds, bulk actions, CSV export and branded PDF
  invoices with VAT.
- **Support tickets** — SLA targets and due times, threaded conversations with attachments,
  canned responses, status/priority/assignee workflow and a full change history.
- **Staff directory** — team members with roles and open-ticket load.
- **Billing automation** — monthly invoice generation and payment reminders that honour the
  configured due, grace and reminder windows and queue messages through the notification
  outbox. Runs automatically when a staff member signs in.

### Infrastructure

- **Network topology** — router → switch → ONU tree with live status.
- **IP address pool** — availability, assignment state and per-subscriber allocation.
- **Device inventory** — CRUD with firmware version, MAC address and uptime tracking.
- **Bandwidth** — rolling 30-day usage per customer and per node.
- **Outages** — severity, affected customers, status and resolution tracking.

### Analytics & audit

- Revenue, growth, ticket-volume and per-node bandwidth charts (Chart.js).
- KPIs: collection rate, churn, active subscribers, ARPU, MRR and average ticket age.
- Revenue breakdowns by package and by node, plus CSV export and a printable statement.
- Leaflet subscriber map with colour-coded connection state.
- Activity/audit log of staff and system actions.

### Customer portal

- Package, usage, balance and open-ticket overview with data-cap warnings.
- Profile editing, notification preferences and usage history.
- Invoice history with online (simulated) payment and PDF download.
- Ticket history, threaded replies with attachments and new-ticket submission.

### Platform

- Two clean access modes: the full **Admin** workspace and a **Customer** portal.
- Global command palette (`Ctrl`/`Cmd` + `K`) for quick navigation and records.
- Dark and light themes with a responsive, mobile-friendly layout.
- Installable PWA with offline fallback and a self-updating service worker.
- Hourly automatic backups, manual snapshots and snapshot import/export.
- Session management and TOTP two-factor authentication.

## Roles & permissions

Access is defined centrally in `js/config.js` and enforced again on the server.

| Capability                        |         Admin        |        Customer       |
| --------------------------------- | :------------------: | :-------------------: |
| Admin workspace & all data        |          ✅          |          —            |
| Customers / packages / billing    |          ✅          |          —            |
| Tickets, network ops, analytics   |          ✅          |          —            |
| Backups, sessions, settings       |          ✅          |          —            |
| Own profile, usage and invoices   |          ✅          |          ✅           |
| Pay own invoices, raise tickets   |          ✅          |          ✅           |
| Manage notification preferences   |          ✅          |          ✅           |

Customer sessions can only read and write their own records — the server sanitises every
state write so a customer can never see or modify another subscriber's data.

## Architecture

```
┌──────────────────────────┐        HTTPS / JSON        ┌──────────────────────────────┐
│   Browser (ES modules)    │  ───────────────────────▶  │   Node server (server.js)     │
│   app.js · modules/       │  ◀───────────────────────  │   REST API + static assets    │
│   store.js · selectors    │   state document + rev     │   node:sqlite (WAL)           │
└──────────────────────────┘                            └──────────────────────────────┘
            │  localStorage cache (offline / demo mode)             │  data/netsphere.db
            └───────────────────────────────────────────────────────┘
```

**State model.** All workspace data lives in a single JSON document (`customers`, `invoices`,
`tickets`, `packages`, `devices`, `outages`, `staff`, `settings`, …) held in `js/store.js` and
derived through `js/selectors.js`. UI modules never touch storage directly — they call
`commit()`, which persists locally and schedules a debounced server sync.

**Sync protocol.** The server stores the document alongside a monotonically increasing
**revision**. Each `PUT /api/state` carries the client's base revision; a mismatch returns
`409` so the client can reconcile instead of clobbering. The document is also mirrored to
`localStorage` for offline use.

**Authentication.** `js/auth.js` is server-first and transparently falls back to a local demo
mode when the API is unreachable, so the UI still works during development.

**Access control.** Roles, page access and management capability live in `js/config.js`
(`ROLES`, `canAccessPage`, `canManage`) and are consumed by `js/permissions.js` and the router
in `js/app.js#showPage`.

**Automation.** `js/automation.js` runs on staff sign-in to generate invoices and queue
reminders according to the configured billing settings.

## Data model

The server maintains the following SQLite tables:

| Table          | Purpose                                                        |
| -------------- | -------------------------------------------------------------- |
| `users`        | Accounts: credentials, role, TOTP secret and status            |
| `sessions`     | Active login sessions and their metadata                        |
| `app_state`    | The workspace document plus its revision counter                |
| `backups`      | Snapshot metadata for the backup/restore feature                |
| `reset_tokens` | One-time password-reset tokens                                  |
| `outbox`       | Simulated email/SMS messages queued for delivery                |
| `audit`        | Append-only audit trail of notable actions                      |

## API reference

All routes exchange JSON. Authentication is required unless marked **public**; **admin**
marks admin-only routes.

| Method   | Path                        | Access  | Description                               |
| -------- | --------------------------- | ------- | ----------------------------------------- |
| `GET`    | `/api/health`               | public  | Liveness probe                            |
| `GET`    | `/api/auth/session`         | public  | Current session (or `null`)               |
| `POST`   | `/api/auth/login`           | public  | Sign in with password (+ optional TOTP)   |
| `POST`   | `/api/auth/logout`          | auth    | Clear the session cookie                  |
| `POST`   | `/api/auth/register`        | public  | Self-service customer sign-up             |
| `POST`   | `/api/auth/forgot`          | public  | Issue a password-reset token              |
| `POST`   | `/api/auth/reset`           | public  | Complete a password reset                 |
| `POST`   | `/api/auth/password`        | auth    | Change the current account password       |
| `POST`   | `/api/auth/2fa/setup`       | auth    | Begin TOTP enrolment                      |
| `POST`   | `/api/auth/2fa/enable`      | auth    | Confirm and enable TOTP                   |
| `POST`   | `/api/auth/2fa/disable`     | auth    | Disable TOTP                              |
| `GET`    | `/api/state`                | auth    | Workspace document + current revision     |
| `PUT`    | `/api/state`                | auth    | Replace state (revision-checked, `409`)   |
| `GET`    | `/api/backups`              | admin   | List backups                              |
| `POST`   | `/api/backups`              | admin   | Create a backup snapshot                  |
| `POST`   | `/api/backups/:id/restore`  | admin   | Restore from a backup                     |
| `GET`    | `/api/backups/:id/download` | admin   | Download a backup file                    |
| `DELETE` | `/api/backups/:id`          | admin   | Delete a backup                           |
| `POST`   | `/api/state/import`         | admin   | Import a state snapshot                   |
| `POST`   | `/api/state/reset`          | admin   | Reset the workspace                       |
| `POST`   | `/api/notify`               | auth    | Queue an email/SMS (simulated)            |
| `GET`    | `/api/outbox`               | admin   | Recent queued messages                    |
| `GET`    | `/api/sessions`             | admin   | Active sessions                           |
| `DELETE` | `/api/sessions`             | admin   | Revoke sessions                           |

## Project structure

```
.
├── index.html              # App shell: login, navigation, all page markup
├── server.js               # Node server: static assets + JSON API + SQLite
├── sw.js                   # Service worker (offline app shell)
├── manifest.webmanifest    # PWA manifest
├── offline.html            # Offline fallback page
├── Dockerfile              # Production image
├── docker-compose.yml      # One-command local deployment
├── css/                    # tokens · base · layout · components · pages
├── js/
│   ├── app.js              # Bootstrap, routing, auth wiring, RBAC, shortcuts
│   ├── api.js              # Fetch client (ApiError, timeouts)
│   ├── auth.js             # Server-first auth with local fallback
│   ├── automation.js       # Billing run + payment reminders
│   ├── config.js           # Constants, roles, demo accounts, page metadata
│   ├── permissions.js      # RBAC helpers for modules
│   ├── store.js            # State, persistence, remote sync
│   ├── selectors.js        # Derived metrics (single source of truth)
│   ├── ui.js               # Toast, modal, confirm, pagination
│   ├── charts.js           # Chart.js theming and lifecycle
│   ├── seed.js             # Deterministic demo dataset
│   ├── watchdog.js         # Boot watchdog for startup diagnostics
│   └── modules/            # One module per feature area
├── e2e/                    # Playwright config + DOM smoke + browser tests
├── assets/                 # PWA icons
└── .github/workflows/      # CI pipeline
```

## Testing

```bash
npm run lint        # ESLint over js/
npm run test:smoke  # jsdom DOM smoke suite (needs the server on :5173)
npm run test:e2e    # Playwright browser suite (auto-starts a server on :5180)
npm test            # lint + smoke + e2e
```

- The **smoke** suite boots the real `js/app.js` inside jsdom and exercises login, CRUD,
  billing, tickets, the portal and role isolation.
- The **E2E** suite drives a real browser (Edge by default, Chromium in CI) against a
  throwaway database on port `5180`.
- CI (`.github/workflows/ci.yml`) runs lint and both suites, and uploads the Playwright report
  on failure.

## Docker

```bash
docker compose up --build     # http://localhost:5173
```

Data persists in the named `netsphere-data` volume. The image runs as a non-root user and
includes a health check against `/api/health`.

## Production deployment

1. **Terminate TLS** at a reverse proxy (nginx, Caddy, Traefik) so `Secure` cookies are used.
2. **Disable demo mode** with `NETSPHERE_DEMO=0` and point `NETSPHERE_DB` at a persistent
   volume.
3. **Back up** `netsphere.db` regularly — the app can also create and restore snapshots from
   **Settings → Backups**.
4. **Replace simulated providers** (payment gateways, email, SMS) with real credentials before
   going live.
5. **Monitor** `/api/health` with your platform's health checks.

## Security

- Passwords are hashed with **scrypt** (`scrypt$salt$hash`); sessions use `HttpOnly`,
  `SameSite=Lax` cookies.
- Every response carries a restrictive **Content-Security-Policy** and hardening headers
  (`X-Content-Type-Options: nosniff`, `X-Frame-Options`, referrer policy).
- **Rate limiting** protects the authentication endpoints; all notable actions are audited.
- **Customer isolation** — server-side sanitisation ensures a customer session can only read
  and write its own records.
- **Backups** are stored as snapshots and can be restored without downtime.
- **Payment gateways, email and SMS are simulated (sandbox).** No real money moves and
  messages are written to the outbox. Wire real providers before production use, and never
  commit secrets.

## Troubleshooting

| Symptom                          | Fix                                                                     |
| -------------------------------- | ----------------------------------------------------------------------- |
| `EADDRINUSE` on start            | The port is busy — run `npm run stop`, or set a different `PORT`.       |
| Blank page on `:5173`            | Hard-refresh (**Ctrl + Shift + R**) to clear the cached service worker. |
| Smoke tests fail immediately     | Start the server first (`npm start`) — the smoke suite targets `:5173`. |
| Map tiles missing                | Check internet access; tiles come from OpenStreetMap.                   |
| Want a clean database            | Stop the server and delete `data/netsphere.db*`.                        |

## FAQ

**Do I need to run a build?** No. Edit the files and reload — the browser loads the ES modules
directly.

**Why no framework?** The project favours a small, dependency-free, long-lived codebase over a
toolchain.

**Can I use a different database?** The server uses the built-in `node:sqlite`; swapping the
storage layer means replacing the thin data-access code in `server.js`.

**Is this production-ready?** The platform is feature-complete and hardened, but payment,
email and SMS integrations are sandbox simulations — wire real providers before real use.

## Limitations & roadmap

- Payment gateways (eSewa / Khalti / Stripe) and email/SMS delivery are sandbox simulations.
- Single-node SQLite storage — ideal for a small ISP; migrate to a networked database for
  multi-instance scale.
- Planned: real provider integrations, multi-tenant support, granular staff permissions and
  scheduled report delivery.

## Contributing

1. Fork the repository and branch from `main`.
2. Keep the project **dependency-free at runtime** and follow the existing module style.
3. Run `npm test` before opening a pull request.
4. Keep generated artifacts and databases (`data/*.db`) out of commits.

## License

MIT © 2026
