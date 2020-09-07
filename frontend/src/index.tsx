import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import "semantic-ui-css/semantic.min.css";
import { Container, Grid } from "semantic-ui-react";
import * as serviceWorker from './serviceWorker';

ReactDOM.render(
  <React.StrictMode>
   <div className="App">
      <Container>
        <Grid>
          <Grid.Row columns="equal" centered>
            <Grid.Column width={16}>
              <App />

            </Grid.Column>
          </Grid.Row>
        </Grid>
      </Container>
    </div>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
