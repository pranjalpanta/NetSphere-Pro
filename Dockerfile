# NetSphere Pro — production image
# Uses Node 24 (built-in node:sqlite, zero runtime dependencies).
FROM node:24-alpine

ENV NODE_ENV=production \
    PORT=5173 \
    NETSPHERE_DB=/app/data/netsphere.db

WORKDIR /app

# Only package metadata is needed at runtime (no production dependencies).
COPY package.json package-lock.json ./

# Application source
COPY index.html offline.html manifest.webmanifest sw.js server.js ./
COPY css ./css
COPY js ./js
COPY assets ./assets
COPY e2e ./e2e

# Persistent data directory owned by the unprivileged node user.
RUN mkdir -p /app/data && chown -R node:node /app

USER node

VOLUME ["/app/data"]
EXPOSE 5173

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget -qO- "http://127.0.0.1:${PORT}/api/health" >/dev/null 2>&1 || exit 1

CMD ["node", "server.js"]
