import React from "react";
import { Container, Grid, Header, Segment, Image } from "semantic-ui-react";
import BottomMenu from "./Menu";
import { server, getKey } from "./Constants";

const Compare = () => {
  const hash = getKey("hash");
  const questionnaire = getKey("questionnaire");
  const resultUrl = server + "image?hash=" + hash;
  const questionnaireUrl =
    server + "image?hash=" + questionnaire + "&questionnaire=true";
  return (
    <>
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header size="large">
                  Tweetlerinizin Kişiliği ile Gerçek Kişiliğiniz Ne Kadar
                  Örtüşüyor?
                </Header>
              </Grid.Column>
            </Grid.Row>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={8}>
                <Image src={resultUrl} size="big" centered />
              </Grid.Column>
              <Grid.Column width={8}>
                <Image src={questionnaireUrl} size="big" centered />
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </Segment>
      <BottomMenu />
    </>
  );
};

export default Compare;
