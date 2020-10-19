import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./App.css";
import Home from "./Home";
import Callback from "./Callback";
import Result from "./Result";
import Share from "./Share";
import Questionnaire from "./Questionnaire";
import Background from "./Background";
import Privacy from "./Privacy";
import Contact from "./Contact";
import Compare from "./Compare";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route path="/callback">
          <Callback />
        </Route>
        <Route path="/result">
          <Result />
        </Route>
        <Route path="/bilimsel-arkaplan">
          <Background />
        </Route>
        <Route path="/gizlilik-bildirimi">
          <Privacy />
        </Route>
        <Route path="/iletisim">
          <Contact />
        </Route>
        <Route path="/compare">
          <Compare />
        </Route>
        <Route exact path="/share/:hash" component={Share} />
        <Route path="/questionnaire">
          <Questionnaire />
        </Route>
        <Route path="*">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
