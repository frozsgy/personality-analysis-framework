import React, { useEffect } from "react";
import { Container, Grid, Header, Segment } from "semantic-ui-react";
import BottomMenu from "./Menu";
import { printBigFive } from "./Result";

const Background = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <>
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header size="large">Bilimsel Arkaplan</Header>
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

                <Header size="large">
                  Kişilik Özellikleri ve Big Five Kişilik Envanteri
                </Header>
                <p>
                  Servisimizde kullanılan Big Five Kişilik envanteri,
                  kişiliğinizin 5 özelliğini esas alarak sonuç çıkarmaktadır.
                  Bunlarla ilgili ayrıntılı bilgiyi aşağıda bulabilirsiniz.
                </p>
                {printBigFive()}
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
