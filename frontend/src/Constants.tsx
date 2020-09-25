export const server = "https://www.tweetkisiligim.xyz/api/"; //;"http://localhost:8080/";//
export const frontend = "https://www.tweetkisiligim.xyz/";

export const getKey = (key = "name") => {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    return urlParams.get(key);
  };

export const openTwitter = () => {
  const url = "https://twitter.com/TweetKisiligim";
  window.open(url);
};