import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Selection from './Selection.js'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Daily Flight Deals</h1>
        </header>
        <div className="Selection-div">
            <Selection />
        </div>
      </div>
    );
  }
}

export default App;
