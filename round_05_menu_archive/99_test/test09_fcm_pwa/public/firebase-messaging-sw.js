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
  apiKey: "AIzaSyDQuRxNY7INGhZwrGnPJO0GAD7egutvvMw",
  authDomain: "push-test-18053.firebaseapp.com",
  projectId: "push-test-18053",
  storageBucket: "push-test-18053.appspot.com",
  messagingSenderId: "372954810910",
  appId: "1:372954810910:web:025e36004a0c08466c3c0f",
  measurementId: "G-QH05RK9QW3",
});

// // Retrieve an instance of Firebase Messaging so that it can handle background
// // messages.
const messaging = firebase.messaging(app);

// 백그라운드에서 수신된 푸시 알림 처리
messaging.onBackgroundMessage((payload) => {
  // console.log(
  //   "onBackgroundMessage",
  //   payload.notification,
  //   self.registration.showNotification
  // );
  // // const notificationTitle = payload.notification.title;
  // // const notificationOptions = {
  // //   body: payload.notification.body,
  // //   icon: payload.notification.image,
  // // };
  self.registration.showNotification("좀떠라..!", {
    body: "왜안뜨냐",
  });
});

// messaging.setBackgroundMessageHandler(function (payload) {
//   // console.log(
//   //   "setBackgroundMessage",
//   //   payload.notification,
//   //   self.registration.showNotification
//   // );
//   // const title = payload.notification.title;
//   // const options = {
//   //   body: payload.notification.body,
//   // };
//   return self.registration.showNotification("좀떠라..@@@@@@!", {
//     body: "왜안뜨냐",
//   });
//   // return self.registration.showNotification(title, options);
// });
