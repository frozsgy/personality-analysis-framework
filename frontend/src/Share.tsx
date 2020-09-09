import React from "react";
import {
  Container,
  Grid,
  Divider,
  Header,
  Segment,
  Image,
} from "semantic-ui-react";
import BottomMenu from "./Menu";
import { server } from "./Constants";
import { Helmet } from "react-helmet";

const Share = (props: any) => {
  const { match } = props;
  let { hash } = match.params;
  const imageUrl = server + "image?hash=" + hash;
  const helmetParts = (
    <Helmet>
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content="Tweetleriniz ile Kişilik Analizi" />
      <meta name="twitter:image" content={imageUrl} />
      <meta
        name="twitter:description"
        content="Bilimsel olarak kanıtlanmış yöntemimiz ile tweetlerinizi analiz edip Twitter'da nasıl bir kişilik temsil ettiğinizi hesaplıyoruz. Makine Öğrenmesi kullanarak yöntemimizi sürekli iyileştiriyoruz."
      />
    </Helmet>
  );
  return (
    <>
      {helmetParts}
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header>Tweetlerinizin Kişiliği Nasıl?</Header>
                <Image src={imageUrl} size="big" centered/>
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

export default Share;
