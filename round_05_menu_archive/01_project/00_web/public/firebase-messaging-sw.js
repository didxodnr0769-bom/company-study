// Scripts for firebase and firebase messaging
importScripts("https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js");
importScripts(
  "https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js"
);

// // Life cycle : install
// self.addEventListener("install", (event) => {
//   console.log("Service Worker: Installed");
//   self.skipWaiting();
// });

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
const app = firebase.initializeApp({
  apiKey: "AIzaSyC96D7QQjowu_2LkEcJ0Ad-wfC87BRRkDo",
  authDomain: "pineone-food-for-me.firebaseapp.com",
  projectId: "pineone-food-for-me",
  storageBucket: "pineone-food-for-me.appspot.com",
  messagingSenderId: "84378549826",
  appId: "1:84378549826:web:ad6cf7f4ee330f6443b7db",
  measurementId: "G-VPLF8B9TRW",
});

self.addEventListener("notificationclick", function (event) {
  event.notification.close(); // 알림 창을 닫음
  console.log("알림 클릭, clients :  ", clients);

  event.waitUntil(
    clients.matchAll({ type: "window" }).then((windowClients) => {
      // 이미 열린 탭이 있는지 확인
      for (var i = 0; i < windowClients.length; i++) {
        var client = windowClients[i];
        if (client.url === "/" && "focus" in client) {
          return client.focus(); // 해당 탭으로 포커스 이동
        }
      }
      // 열린 탭이 없다면 새로운 탭에서 애플리케이션 열기
      if (clients.openWindow) {
        return clients.openWindow("/");
      }
    })
  );
});

// // Retrieve an instance of Firebase Messaging so that it can handle background
// // messages.
const messaging = firebase.messaging(app);

// 백그라운드에서 수신된 푸시 알림 처리
messaging.onBackgroundMessage((payload) => {
  const notificationTitle = payload.data.title;
  const notificationOptions = {
    body: payload.data.body,
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});
