import { useEffect } from "react";
import "./firebase-messaging-sw.js";
import { requestPermission } from "./firebase-messaging-sw.js";

function App() {
  useEffect(() => {
    requestPermission();
  }, []);

  return (
    <div>
      앱 컨텐츠
      <button onClick={() => {}}>푸시 테스트</button>
    </div>
  );
}

export default App;
