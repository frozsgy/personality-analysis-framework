import React from "react";
import {
  Container,
  Grid,
  Form,
  Button,
  Divider,
  Header,
  Segment,
  Icon,
} from "semantic-ui-react";
import fetch from "isomorphic-unfetch";
import BottomMenu from "./Menu";
import { server } from "./Constants";



const Home = () => {
    const Login = (e: { preventDefault: () => void; }) => {
        e.preventDefault();
        fetch(server, {
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
            window.location = response!.url;
          })
          .catch((e) => {
            console.log(e.message);
          });
      };
    
    //const handleItemClick = (e, { url }) => history.push(url);



  return (
    <>
      <Segment>
        <Container>
          <Grid>
            <Grid.Row columns="equal" centered>
              <Grid.Column width={16}>
                <Header>Tweetlerinizin Kişiliği Nasıl?</Header>
                <p>
                  Bilimsel olarak kanıtlanmış yöntemimiz ile tweetlerinizi
                  analiz edip Twitter'da nasıl bir kişilik temsil ettiğinizi
                  hesaplıyoruz. Makine Öğrenmesi kullanarak yöntemimizi sürekli
                  iyileştiriyoruz.
                </p>
                <p>
                  Kişiliğinizi görüntülemek için Twitter hesabınızla giriş
                  yapın:{" "}
                </p>
                <Form>
                  <Form.Field>
                    <Button color="twitter" size="large" onClick={Login}>
                      <Icon name="twitter" /> Twitter ile Giriş Yapın
                    </Button>
                  </Form.Field>
                  <p>Yalnızca tweetlerinizi okuma izni istiyoruz.</p>
                </Form>
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

export default Home;
