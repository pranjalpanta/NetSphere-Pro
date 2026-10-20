# AGENTS.md — NetSphere Pro

Guidance for AI agents and contributors working in this repository.

## Project

Browser-based ISP management system. Vanilla ES modules frontend (no framework, no build
step) + a zero-dependency Node server (`server.js`) using the built-in `node:sqlite`
database. Requires **Node 24+** (for `node:sqlite`).

## Commands

| Command              | Purpose                                                     |
| -------------------- | ----------------------------------------------------------- |
| `npm start`          | Run the server on http://localhost:5173 (`node server.js`)  |
| `npm run lint`       | ESLint over `js/` — run after every change                  |
| `npm run test:smoke` | jsdom DOM smoke suite (requires the server running :5173)   |
| `npm run test:e2e`   | Playwright browser tests (auto-starts a server on :5180)    |
| `npm test`           | lint + smoke + e2e                                          |

Always run `npm run lint` and `node --check <file>` after editing JS. Run the smoke and
e2e suites before declaring work complete.

## Conventions

- **No new runtime dependencies.** Keep the app and server dependency-free. `devDependencies`
  (eslint, prettier, jsdom, @playwright/test) are for tooling only.
- **No comments** in source unless they clarify non-obvious intent (module headers are fine).
- **No build step.** Edit files directly; the browser loads ES modules as-is.
- Follow existing module style: imports at top, pure helpers first, `export function render()`
  and `export function bind()` per feature module.
- Keep data flowing through `js/store.js` (state) and `js/selectors.js` (derived values).
  Persist via `commit()`; never write `localStorage` directly.
- Preserve UTF-8 in CSS/HTML. Do not use PowerShell to write files (it corrupts encoding and
  `Set-Content -Encoding utf8NoBOM` is unavailable); use the editor tools.

## Architecture notes

- `server.js`: tables `users`, `sessions`, `app_state`, `backups`, `reset_tokens`, `outbox`,
  `audit`. API routes are declared with `route(method, path, handler, options)` — pass options
  as the 4th argument (`{ public: true }` / `{ admin: true }`) or auth is required by default.
- State sync uses a revision counter; conflicting `PUT /api/state` returns `409`.
- `js/auth.js` is server-first and falls back to local demo mode when the API is unreachable.
- RBAC lives in `js/config.js` (`ROLES`, `canAccessPage`, `canManage`) and
  `js/permissions.js` (`can`, `isStaff`). Gate pages in `app.js#showPage` and actions in modules.
- Billing automation is in `js/automation.js`, invoked when a non-customer signs in.

## Testing tips

- Restart the server after any `server.js` change. Kill only the PID owning port 5173:
  `Get-NetTCPConnection -LocalPort 5173 -State Listen | Select -Expand OwningProcess`.
  (Killing all node processes also kills the agent shell.)
- `e2e/playwright.config.js` uses the local Edge channel in dev and installs Chromium in CI.
- Demo accounts are seeded idempotently from `DEMO_ACCOUNTS` in `js/config.js`.

## Constraints

- Payment gateways, email and SMS are simulated (sandbox) — keep them clearly marked.
- Do not commit `data/*.db`, secrets, or generated test artifacts (see `.gitignore`).
