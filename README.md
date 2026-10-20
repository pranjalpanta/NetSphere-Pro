# NetSphere Pro — ISP Management System

A complete ISP operations platform: subscriber records, package plans, VAT invoicing with
partial payments and refunds, support tickets with SLA tracking, staff, network operations,
analytics, billing automation, and a customer self-service portal.

The frontend is **vanilla ES modules** (no framework, no build step) backed by a
**zero-dependency Node server** with built-in SQLite persistence, scrypt password hashing,
session cookies, TOTP 2FA, backups, an audit trail and a notification outbox. It is a
installable **PWA** with offline app-shell caching.

## Quick start

```bash
npm start        # serves the app at http://localhost:5173
```

Open http://localhost:5173. The database is created automatically at `data/netsphere.db`.

### Demo accounts

| Role     | Username   | Password       |
| -------- | ---------- | -------------- |
| Admin    | `admin`    | `admin123`     |
| Customer | `customer` | `customer123`  |

Pick a role on the login screen — credentials are prefilled for the demo.

### Environment variables

| Variable           | Default                 | Purpose                                   |
| ------------------ | ----------------------- | ----------------------------------------- |
| `PORT`             | `5173`                  | HTTP port                                 |
| `NETSPHERE_DB`     | `data/netsphere.db`     | SQLite database path                      |
| `NETSPHERE_DEMO`   | `1`                     | `0` disables seeded demo accounts         |

## Features

**Operations**
- Dashboard with revenue trend, package mix, recent payments and system snapshot
- Customer CRUD, search/filter, pagination, bulk delete, CSV import/export
- Packages with subscriber reassignment on deletion
- Billing: generation, status lifecycle (unpaid → partial → overdue → paid), partial
  payments (cash / bank / simulated gateways), credit notes, refunds, bulk actions, CSV
  export and PDF invoices
- Support tickets: SLA targets, conversation threads with attachments, canned responses,
  status/priority/assignment workflow and history
- Staff directory with roles and open-ticket load
- **Billing automation**: monthly invoice generation and payment reminders honouring
  due/grace/reminder day settings, queued through the notification outbox

**Infrastructure**
- Network topology tree (router → switch → ONU) with live status
- IP address pool, device CRUD with firmware/uptime, 30-day bandwidth usage
- Outage management with severity, affected customers and resolution tracking

**Analytics & audit**
- Revenue, growth, ticket-volume and per-node bandwidth charts (Chart.js)
- Collection rate, churn, active subscribers, ARPU, MRR, staff performance
- Revenue by package and by node; CSV export and printable statement
- Leaflet subscriber map and an activity/audit log

**Customer portal**
- Package, usage, balance and open-ticket overview with cap warnings
- Profile editing, notification preferences, usage history
- Invoice history with online (simulated) payment and PDF download
- Ticket history, threaded replies with attachments and new ticket submission

**Platform**
- Two clean access modes: full **Admin** workspace and a read/write **Customer** portal
- Global command search (`Ctrl/Cmd + K`)
- Dark/light themes, responsive layout, PWA install + offline fallback
- Server-side SQLite state with revisioned sync, hourly auto-backups, snapshot
  import/export, session management and TOTP 2FA

## Project structure

```
.
├── index.html              # App shell: login, navigation, all page markup
├── server.js               # Node server: static assets + JSON API + SQLite
├── sw.js                   # Service worker (offline app shell)
├── manifest.webmanifest    # PWA manifest
├── offline.html            # Offline fallback page
├── css/                    # tokens, base, layout, components, pages
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
│   └── modules/            # One module per feature area
├── e2e/                    # Playwright config + DOM smoke + browser tests
└── assets/
```

## Testing

```bash
npm run lint        # ESLint over js/
npm run test:smoke  # jsdom DOM smoke suite (needs the server on :5173)
npm run test:e2e    # Playwright browser tests (starts its own server on :5180)
npm test            # lint + smoke + e2e
```

The smoke suite boots the real `js/app.js` in jsdom; Playwright drives Edge locally
(Chromium in CI). See `.github/workflows/ci.yml`.

## Docker

```bash
docker compose up --build     # http://localhost:5173, data in the netsphere-data volume
```

## Security notes

- Passwords are hashed with **scrypt** and sessions use `HttpOnly` cookies.
- Security headers and a restrictive CSP are applied to all responses.
- Payment gateways, email and SMS are **simulated** (sandbox) — no real money moves and
  messages are written to the outbox. Wire real providers before production use.
- Serve behind HTTPS in production so secure cookies are enabled. Never commit secrets.

## License

MIT © 2026
