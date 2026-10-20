/* NetSphere Pro service worker: app-shell caching + offline fallback. */
const VERSION = "netsphere-v2";
const SHELL = [
    "/",
    "/index.html",
    "/offline.html",
    "/manifest.webmanifest",
    "/assets/icon.svg",
];

self.addEventListener("install", (event) => {
    event.waitUntil(
        caches
            .open(VERSION)
            .then((cache) => cache.addAll(SHELL.map((url) => new Request(url, { cache: "reload" }))))
            .then(() => self.skipWaiting())
            .catch(() => self.skipWaiting()),
    );
});

self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches
            .keys()
            .then((keys) => Promise.all(keys.filter((key) => key !== VERSION).map((key) => caches.delete(key))))
            .then(() => self.clients.claim()),
    );
});

self.addEventListener("fetch", (event) => {
    const { request } = event;
    if (request.method !== "GET") return;

    const url = new URL(request.url);
    if (url.origin !== self.location.origin) return;

    if (url.pathname.startsWith("/api/")) {
        event.respondWith(
            fetch(request).catch(
                () =>
                    new Response(JSON.stringify({ error: "You are offline. This action needs a connection." }), {
                        status: 503,
                        headers: { "Content-Type": "application/json; charset=utf-8" },
                    }),
            ),
        );
        return;
    }

    if (request.mode === "navigate") {
        event.respondWith(
            fetch(request)
                .then((response) => {
                    const copy = response.clone();
                    caches.open(VERSION).then((cache) => cache.put("/index.html", copy));
                    return response;
                })
                .catch(() => caches.match("/index.html").then((cached) => cached || caches.match("/offline.html"))),
        );
        return;
    }

    // Network-first for same-origin assets so updates appear immediately;
    // fall back to the cache when offline.
    event.respondWith(
        fetch(request)
            .then((response) => {
                if (response && response.status === 200 && response.type === "basic") {
                    const copy = response.clone();
                    caches.open(VERSION).then((cache) => cache.put(request, copy));
                }
                return response;
            })
            .catch(() => caches.match(request).then((cached) => cached || caches.match("/offline.html"))),
    );
});

// Allow the page to trigger an immediate update of the running worker.
self.addEventListener("message", (event) => {
    if (event.data === "SKIP_WAITING") self.skipWaiting();
});
