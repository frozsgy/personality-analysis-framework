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

            <Header size="medium">Sonuçlarınız arasında fark mı var?</Header>
            <p>
              Eğer Twitter hesabınızdaki kişiliğiniz ile anket sonucundaki
              kişiliğiniz arasında ciddi fark varsa, bunun iki sebebi olabilir:
            </p>
            <p>
              <ol>
                <li>
                  Twitter hesabınızda gerçek kişiliğinizden farklı bir kişilik
                  gösteriyorsunuz
                </li>
                <li>
                  Sizin kişilik özelliklerinize sahip birine dair veriye daha
                  önce ulaşamamışız
                </li>
              </ol>
            </p>
            <p>
              Eğer sebebin birincisi olduğunu düşünüyorsanız, sorun yok! Ancak
              sebebin ikinci madde olduğunu düşünüyorsanız,{" "}
              <strong>size çok teşekkür ederiz</strong>! Anketimizi doldurarak
              yapay zeka modelimizin iyileştirilmesine katkıda bulundunuz, veri
              bilimi bu katkınızı unutmayacak :)
            </p>
            <p></p>
          </Grid>
        </Container>
      </Segment>
      <BottomMenu />
    </>
  );
};

export default Compare;
