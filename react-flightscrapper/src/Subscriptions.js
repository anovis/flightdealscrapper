import { ListGroup,ListGroupItem, Button,Alert } from 'react-bootstrap';
import React, { Component } from 'react';
var axios = require('axios');


export default class Subscriptions extends React.Component {
  constructor(props) {
    super(props);
    this.state = {email: '',
                  subscriptions: [],
                  noemails: false};
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({email: event.target.value});
  }

  handleSubmit(event) {
    axios.get('https://woysf8pmu6.execute-api.us-east-1.amazonaws.com/api/subscriptions/' + this.state.email)
        .then((response) => {
         if (response.data.length ==0){
            this.setState({noemails:true})
            }
          else{
            this.setState({noemails:false})
            }
          this.setState({subscriptions: response.data})
        })
        .catch((error) => {console.log(error)})
    event.preventDefault();
  }

  render() {
    var subscription_list = [];
    for (var i=0; i < this.state.subscriptions.length; i++){
        subscription_list.push(<li className="li-sub"><a className="li-sub-a"> {this.state.subscriptions[i]} </a></li>)
    }

    return (
    <div>
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <label>Enter Email address you used to sign up</label>
              <input className="form-styling" type="email" id="email" value={this.state.email} onChange={this.handleChange} placeholder="Email" />

            </div>
             <input className="btn btn-default" type="submit" value="Submit" />

          </form>
          <ul className="ul-sub">
        {subscription_list}
       </ul>
       {this.state.noemails && alert}
       </div>
    );
  }
}

const alert = <Alert bsStyle="warning" >
                            <h4>No Subscriptions found for this email</h4>
                            <p>Try with a different email or Signup</p>
                          </Alert>
