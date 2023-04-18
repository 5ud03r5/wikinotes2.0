export const getItems = async (itemPages, endpoint, limit, tags, search) => {
  let construct = "/?page=" + itemPages + "&limit=" + limit;
  if (search != undefined && tags != undefined) {
    construct =
      "/?page=" +
      itemPages +
      "&limit=" +
      limit +
      "&search=" +
      search +
      "&tags=" +
      tags.map((tag) => {
        return tag.id;
      });
  } else if (tags != undefined) {
    construct =
      "/?page=" +
      itemPages +
      "&limit=" +
      limit +
      "&tags=" +
      tags.map((tag) => {
        return tag.id;
      });
  } else if (search != undefined) {
    construct = "/?page=" + itemPages + "&limit=" + limit + "&search=" + search;
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

export const getItem = async (id) => {
  const response = await fetch(
    import.meta.env.VITE_BACKEND + "/articles/" + id
  );
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
