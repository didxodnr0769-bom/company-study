import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceWorker.register("/firebase-messaging-sw.js").then(
      function (registration) {
        // 등록 성공
        console.log(
          "ServiceWorker registration successful with scope: ",
          registration
        );
      },

      function (err) {
        // 등록 실패
        console.log("ServiceWorker registration failed: ", err);
      }
    );
  });
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
