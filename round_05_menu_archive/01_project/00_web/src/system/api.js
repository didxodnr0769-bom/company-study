// const API_SERVER_URL = "http://192.168.0.17:3000";
const API_SERVER_URL = "https://dont-go-cat-yang.koyeb.app";

export const createRegistToken = (token) => {
  return fetch(`${API_SERVER_URL}/token/regist`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      token,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .catch((error) =>
      console.error("There was a problem with your fetch operation:", error)
    );
};

export const getMenuList = () => {
  return fetch(`${API_SERVER_URL}/menu/list`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .catch((error) =>
      console.error("There was a problem with your fetch operation:", error)
    );
};
