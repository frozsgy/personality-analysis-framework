import React from "react";
import {
  Container,
  Grid,
  Header,
  Segment,
  Button,
  Icon,
} from "semantic-ui-react";
import BottomMenu from "./Menu";
import { openTwitter } from "./Constants";

export const contactDetails = (
  <>
    <p>
      Uygulama hakkında sorularınız için bizimle Twitter veya
      e-mail üzerinden iletişime geçebilirsiniz.
    </p>

    <Button.Group widths="8" fluid>
      <Button color="purple" floated="right">
        <Icon name="mail outline" />
        tweetkisiligim@gmail.com
      </Button>

      <Button color="twitter" size="large" onClick={() => openTwitter()}>
        <Icon name="twitter" /> @TweetKisiligim
      </Button>
    </Button.Group>
  </>
);

const Contact = () => {
  return (
    <>
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header size="large">İletişim</Header>

                {contactDetails}
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </Segment>
      <BottomMenu />
    </>
  );
};

export default Contact;
