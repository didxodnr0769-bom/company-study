if ("serviceWorker" in navigator) {
  navigator.serviceWorker
    .register("./service-worker.js")
    .then((reg) => {
      console.log("Service Worker Registered.", reg);
    })
    .catch((err) => {
      console.log("Service Worker Not Registered.", err);
    });
}

const requestAPI = async () => {
  const response = await fetch("http://localhost:5500/web/mock/fallback.json");

  // 응답이 성공적인지 확인
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }

  // 응답 데이터를 JSON으로 변환
  const data = await response.json();

  console.log("data", data);
  return response;
};
