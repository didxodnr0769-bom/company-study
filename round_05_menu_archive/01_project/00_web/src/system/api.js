const API_SERVER_URL = "http://localhost:5001";

const getMenuList = () => {
  return fetch(`${API_SERVER_URL}/mock/menu/list`)
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

export { getMenuList };
