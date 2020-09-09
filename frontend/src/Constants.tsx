export const server = "https://personality-api.ozanalpay.com/";
export const frontend = "https://personality.ozanalpay.com/";

export const getKey = (key = "name") => {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    return urlParams.get(key);
  };