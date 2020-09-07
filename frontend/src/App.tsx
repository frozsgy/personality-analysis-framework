import React from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import './App.css';
import Home from "./Home";
import Callback from "./Callback";
import Result from "./Result";

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
        
        <Route path="*">404 not found</Route>
      </Switch>
    </Router>
  );
}

export default App;
