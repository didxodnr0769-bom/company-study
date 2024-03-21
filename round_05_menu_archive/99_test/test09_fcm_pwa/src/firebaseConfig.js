import firebase from "firebase/app";
import "firebase/messaging";
import { vapidKey } from "./constant.ignore";

const firebaseConfig = {
  apiKey: "AIzaSyDQuRxNY7INGhZwrGnPJO0GAD7egutvvMw",
  authDomain: "push-test-18053.firebaseapp.com",
  projectId: "push-test-18053",
  storageBucket: "push-test-18053.appspot.com",
  messagingSenderId: "372954810910",
  appId: "1:372954810910:web:025e36004a0c08466c3c0f",
  measurementId: "G-QH05RK9QW3",
};

const app = firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging(app);

export function requestPermission() {
  console.log("request  permission");
  Notification.requestPermission().then((permission) => {
    if (permission === "granted") {
      messaging
        .getToken({ vapidKey })
        .then((token) => {
          console.log(`푸시 토큰 발급 완료 : ${token}`);
          messaging.onMessage((payload) => {
            console.log("푸시 알림 수신 - 포그라운드", payload);
            // alert("알림:" + payload.notification.body);
          });
        })
        .catch((err) => {
          console.log("푸시 토큰 가져오는 중에 에러 발생", err);
        });
    } else if (permission === "denied") {
      console.log("푸시 권한 차단");
    }
  });
}
