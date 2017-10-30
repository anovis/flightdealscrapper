import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Selection from './Selection.js'
import Signup from './Signup.js'
import {Button} from 'react-bootstrap';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {signup:false};
    this.toggleSignup = this.toggleSignup.bind(this);
  }

  toggleSignup(event) {
    console.log(this.state)
    this.setState({signup: !this.state.signup});
   }

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
       <div className="form-group col-md-4">
       </div>
       <Button type="button" onClick={this.toggleSignup}>
         Sign Up
       </Button>
        <div className="form-group col-md-4">
            <div className="Form-div">
            {this.state.signup && <Signup />}
            </div>
        </div>

        <div className="form-group col-md-4">
        </div>

      </div>
    );
  }
}

export default App;
