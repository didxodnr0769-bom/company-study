import { useEffect } from "react";
import { requestPermission } from "./firebaseConfig.js";

function App() {
  useEffect(() => {
    requestPermission();
  }, []);

  return (
    <div className="App">
      <h1>FCM TEST</h1>
    </div>
  );
}

export default App;
