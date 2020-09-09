import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./App.css";
import Home from "./Home";
import Callback from "./Callback";
import Result from "./Result";
import Share from "./Share";

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
        <Route exact path="/share/:hash" component={Share} />

        <Route path="*">404 not found</Route>
      </Switch>
    </Router>
  );
}

export default App;
