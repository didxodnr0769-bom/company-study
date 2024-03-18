// service-worker.js
var CACHE_NAME = "resoucre-cache-v17";
var urlsToCache = [
  // "./index.html",
  // "./css/main.css",
  // "./js/main.js",
  "./mock/fallback.json",
];

// Life cycle : install
self.addEventListener("install", (event) => {
  console.log("Service Worker: Installed");
  self.skipWaiting();

  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Life cycle : activate
self.addEventListener("activate", (event) => {
  console.log("Service Worker: Activated!!!");
  // 기존 캐시 삭제
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Life cycle : fetch
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((res) => {
      if (res) {
        return res;
      }

      return fetch(event.request).then((res) => {
        return res;
      });
    })
  );
});
