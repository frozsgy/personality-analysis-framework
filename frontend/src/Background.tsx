import React from "react";
import { Container, Grid, Header, Segment } from "semantic-ui-react";
import BottomMenu from "./Menu";

const Background = () => {
  return (
    <>
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header size='large'>Bilimsel Arkaplan</Header>
                <p>
                  Bu servis, Clustering based Personality Prediction on Turkish
                  Tweets (Tutaysalgir, Karagoz, & Toroslu, 2019) başlıklı makale
                  temel alarak geliştirilmiştir. Ayrıntılı bilgi için makaleye
                  şu adresten erişebilirsiniz:{" "}
                  <a
                    href="https://ieeexplore.ieee.org/abstract/document/9073214"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    https://ieeexplore.ieee.org/abstract/document/9073214
                  </a>
                </p>
              </Grid.Column>
            </Grid.Row>
          </Grid>
        </Container>
      </Segment>
      <BottomMenu />
    </>
  );
};

export default Background;
