import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import "semantic-ui-css/semantic.min.css";
import { Container, Grid, Image } from "semantic-ui-react";
import * as serviceWorker from "./serviceWorker";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.min.css";
import { frontend } from "./Constants";
import CookieConsent from "react-cookie-consent";


ReactDOM.render(
  <React.StrictMode>
    <div className="App">
      <Container>
        <Grid>
          <Grid.Row columns="equal" centered>
            <Grid.Column width={12} className="logo" stackable>
              <Image
                src="https://www.metu.edu.tr/sites/all/themes/odtu/images/odtu-logo-en.svg"
                as="a"
                size="medium"
                href={frontend}
                target="_blank"
                className="left"
              />

              {/*(<Button
                  color="twitter"
                  size="medium"
                  onClick={() => openTwitter()}
                  className="right"
                >
                  <Icon name="twitter" /> @TweetKisiligim
                </Button>)*/}
            </Grid.Column>
          </Grid.Row>

          <Grid.Row columns="equal" centered>
            <Grid.Column width={12}>
              <App />
              <ToastContainer />
            </Grid.Column>
          </Grid.Row>
        </Grid>
      </Container>
    </div>

    <CookieConsent acceptOnScroll={true} buttonText={"Anladım"}>
      Sitemizi en verimli şekilde kullanabilmeniz ve kullanıcı
      deneyiminizi iyileştirebilmek için çerezler kullanmaktayız. Çerez
      kullanılmasını tercih etmezseniz tarayıcınızın ayarlarından çerezleri
      silebilir ya da engelleyebilirsiniz. 
    </CookieConsent>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
