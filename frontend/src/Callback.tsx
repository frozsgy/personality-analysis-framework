import React from "react";
import { Container, Grid, Header, Segment } from "semantic-ui-react";
import { useHistory } from "react-router-dom";
import fetch from "isomorphic-unfetch";
import BottomMenu from "./Menu";
import { server, getKey } from "./Constants";

const Home = () => {
  const history = useHistory();

  const oauth_token = getKey("oauth_token");
  const oauth_verifier = getKey("oauth_verifier");

  const startAnalysis = () => {
    const autoShare = localStorage.getItem("autoShare") === "true";

    fetch(
      server +
        "callback?oauth_token=" +
        oauth_token +
        "&oauth_verifier=" +
        oauth_verifier +
        "&auto_share=" +
        autoShare,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
      .then((r) => {
        if (r.ok) {
          return r;
        }
        if (r.status === 401 || r.status === 403 || r.status === 500) {
          return Promise.reject(new Error("Unknown error occurred"));
        }
      })
      .then((r) => r!.json())
      .then((response) => {
        history.push(response!.url);
      })
      .catch((e) => {
        console.log(e.message);
      });
  };

  startAnalysis();
  return (
    <>
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header>Tweetlerinizin Kişiliği Nasıl?</Header>
                <p>Tweetleriniz analiz ediliyor</p>
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </Segment>
      <BottomMenu />
    </>
  );
};

export default Home;
