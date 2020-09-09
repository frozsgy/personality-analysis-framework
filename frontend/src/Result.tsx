import React, { useState } from "react";
import {
  Container,
  Grid,
  Divider,
  Header,
  Segment,
  Progress,
} from "semantic-ui-react";
import fetch from "isomorphic-unfetch";
import BottomMenu from "./Menu";
import { server, getKey } from "./Constants";
import RadarChart from "react-svg-radar-chart";
import "react-svg-radar-chart/build/css/index.css";

const Result = () => {
  const [loaded, setLoaded] = useState({ loaded: false });
  const [scores, setScores] = useState({
    o: 0.0,
    c: 0.0,
    e: 0.0,
    a: 0.0,
    n: 0.0,
  });

  let percent = 30;

  const id = getKey("id");
  const hash = getKey("hash");

  const data = [
    {
      data: {
        openness: scores.o / 4,
        conscientiousness: scores.c / 4,
        extraversion: scores.e / 4,
        agreeableness: scores.a / 4,
        neuroticism: scores.n / 4,
      },
      meta: { color: "green" },
    },
  ];

  const captions = {
    // columns
    openness: "Açıklık",
    conscientiousness: "Sorumluluk",
    extraversion: "Dışadönüklük",
    agreeableness: "Uyumluluk",
    neuroticism: "Nevrotiklik",
  };

  const startAnalysis = () => {
    fetch(server + "result?id=" + id + "&hash=" + hash, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
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
        if (response.status === 200) {
          if (response.finished === true) {
            const response_scores = response.score;
            if (scores.o !== response_scores.o) {
              setLoaded({ loaded: true });
              setScores({
                o: response_scores.o,
                c: response_scores.c,
                e: response_scores.e,
                a: response_scores.a,
                n: response_scores.n,
              });
            }
          } else {
            console.log("waiting");
            percent += 5;
            setTimeout(startAnalysis, 5000);
          }
        } else {
          console.log("error");
        }
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
              <Grid.Column width={8}>
                <Header>Tweetlerinizin Kişiliği Nasıl?</Header>
                {scores.o !== 0.0 && (
                  <RadarChart captions={captions} data={data} size={450} />
                )}
                {scores.o === 0.0 && (
                  <>
                    <p>Tweetleriniz analiz ediliyor</p>
                    <Progress
                      percent={loaded.loaded ? 100 : percent}
                      autoSuccess
                      active
                    />
                  </>
                )}
                <Divider />
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </Segment>
      <BottomMenu />
    </>
  );
};

export default Result;
