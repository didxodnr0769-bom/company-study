import firebase from "firebase/app";
import "firebase/messaging";
import { vapidKey } from "./constant.ignore";

const firebaseConfig = {
  apiKey: "AIzaSyC96D7QQjowu_2LkEcJ0Ad-wfC87BRRkDo",
  authDomain: "pineone-food-for-me.firebaseapp.com",
  projectId: "pineone-food-for-me",
  storageBucket: "pineone-food-for-me.appspot.com",
  messagingSenderId: "84378549826",
  appId: "1:84378549826:web:ad6cf7f4ee330f6443b7db",
  measurementId: "G-VPLF8B9TRW",
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);

// 서비스 워커 등록
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceWorker.register("/firebase-messaging-sw.js").then(
      function (registration) {
        // 등록 성공
        console.log("서비스워커가 등록되었습니다.", registration.scope);
      },

      function (err) {
        // 등록 실패
        console.error("ServiceWorker registration failed: ", err);
      }
    );
  });
}

const messaging = firebase.messaging(app);

/**
 * 푸시 알림 권한 요청
 */
export function requestPermission() {
  Notification.requestPermission().then((permission) => {
    if (permission === "granted") {
      messaging
        .getToken({ vapidKey })
        .then((token) => {
          console.log(`푸시 토큰 발급 완료 : ${token}`);
          messaging.onMessage((payload) => {
            console.log("푸시 알림 수신 - 포그라운드", payload);
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
