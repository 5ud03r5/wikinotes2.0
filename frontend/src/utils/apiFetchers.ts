import { Tag } from "./interfaces";

const BACKEND = "http://127.0.0.1:8000";

export const getItems = async (
  itemPages: number,
  endpoint: string,
  limit: number,
  tags?: Tag[],
  search?: string
) => {
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

  const response = await fetch(BACKEND + "/" + endpoint + construct);
  if (!response.ok) {
    throw Error("Something went wrong");
  }
  const data = await response.json();
  return [data.data, data.total];
};

export const getTags = async () => {
  const response = await fetch(BACKEND + "/tags/");
  if (!response.ok) {
    throw Error("Something went wrong");
  }
  const data = await response.json();
  return data;
};

export const getItem = async (id: string) => {
  const response = await fetch(BACKEND + "/articles/" + id);
  if (!response.ok) {
    throw Error("Something went wrong");
  }
  const data = await response.json();
  return data;
};

export const createItem = async (endpoint: string, body: object) => {
  const response = await fetch(BACKEND + "/" + endpoint + "/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!response.ok) {
    throw Error("Something went wrong");
  }
};

export const removeItem = async (endpoint: string, id: string) => {
  const response = await fetch(BACKEND + "/" + endpoint + "/" + id, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  });
  if (!response.ok) {
    throw Error("Something went wrong");
  }
};
