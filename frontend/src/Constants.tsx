export const server = "http://localhost:8080/";

export const getKey = (key = "name") => {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    return urlParams.get(key);
  };