export const getItems = async (itemPages, endpoint, limit) => {
  const response = await fetch(
    import.meta.env.VITE_BACKEND +
      "/" +
      endpoint +
      "/" +
      `?page=${itemPages.value}` +
      "&limit=" +
      limit
  );
  if (!response.ok) {
    throw Error("Something went wrong");
  }
  const data = await response.json();
  console.log(data);
  return [data.data, data.total];
};

export const createItem = async (endpoint, body) => {
  const response = await fetch(
    import.meta.env.VITE_BACKEND + "/" + endpoint + "/",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    }
  );
  if (!response.ok) {
    throw Error("Something went wrong");
  }
  console.log(await response.json());
};
