// Scripts for firebase and firebase messaging
importScripts("https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js");
importScripts(
  "https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js"
);

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
  apiKey: "AIzaSyDQuRxNY7INGhZwrGnPJO0GAD7egutvvMw",
  authDomain: "push-test-18053.firebaseapp.com",
  projectId: "push-test-18053",
  storageBucket: "push-test-18053.appspot.com",
  messagingSenderId: "372954810910",
  appId: "1:372954810910:web:025e36004a0c08466c3c0f",
  measurementId: "G-MLW61V653M",
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();

// 백그라운드에서 수신된 푸시 알림 처리
messaging.onBackgroundMessage((payload) => {
  console.log("???", payload.notification, self.registration.showNotification);
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: payload.notification.image,
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});
