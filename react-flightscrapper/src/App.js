import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Selection from './Selection.js'
import Signup from './Signup.js'
import Subscriptions from './Subscriptions.js'
import {Button,ButtonGroup,ButtonToolbar} from 'react-bootstrap';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {signup:false,
                  flights: true,
                  subscription: false
            };
    this.toggleSignup = this.toggleSignup.bind(this);
    this.toggleFlights = this.toggleFlights.bind(this);
    this.toggleSubscription = this.toggleSubscription.bind(this);

  }

    toggleSignup(event) {
       this.setState({signup: !this.state.signup,
                      flights: false,
                      subscription: false});
    }
    toggleFlights(event) {
       this.setState({signup: false,
                      flights: !this.state.flights,
                      subscription: false});
      }
    toggleSubscription(event) {
       this.setState({signup: false,
                      flights: false,
                      subscription: !this.state.subscription});
     }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Daily Flight Deals</h1>
        </header>
        <div className="container">
          <div className="frame">
            <div className="nav">
              <ul className= "links">
                <li className="nav-li"><Button bsStyle="primary" type="button" onClick={this.toggleFlights}> Today's Deals </Button></li>
                <li className="nav-li"><Button bsStyle="primary" type="button" onClick={this.toggleSignup}> Sign Up </Button></li>
                <li className="nav-li"><Button bsStyle="primary" type="button" onClick={this.toggleSubscription}> View Subscriptions </Button></li>
              </ul>
             </div>

                <div className="Form-div">
                    {this.state.flights && <Selection />}
                    {this.state.signup && <Signup />}
                    {this.state.subscription && <Subscriptions />}
                </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
