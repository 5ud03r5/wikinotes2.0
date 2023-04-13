export const getItems = async (itemPages, endpoint, limit) => {
  let construct = "";
  if (itemPages && limit) {
    construct = "/?page=" + itemPages + "&limit=" + limit;
  }
  const response = await fetch(
    import.meta.env.VITE_BACKEND + "/" + endpoint + construct
  );
  if (!response.ok) {
    throw Error("Something went wrong");
  }
  const data = await response.json();
  return [data.data, data.total];
};

export const getTags = async () => {
  const response = await fetch(import.meta.env.VITE_BACKEND + "/tags/");
  if (!response.ok) {
    throw Error("Something went wrong");
  }
  const data = await response.json();
  return data;
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
};

export const removeItem = async (endpoint, id) => {
  const response = await fetch(
    import.meta.env.VITE_BACKEND + "/" + endpoint + "/" + id,
    {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
    }
  );
  if (!response.ok) {
    throw Error("Something went wrong");
  }
};
