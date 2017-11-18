import { ListGroup,ListGroupItem, Button } from 'react-bootstrap';
import React, { Component } from 'react';
var axios = require('axios');


export default class Subscriptions extends React.Component {
  constructor(props) {
    super(props);
    this.state = {email: '',
                  subscriptions: []};
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({email: event.target.value});
  }

  handleSubmit(event) {
    axios.get('http://127.0.0.1:5000/subscriptions/' + this.state.email)
        .then((response) => {
          this.setState({subscriptions: response.data.subscriptions})
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
       </div>
    );
  }
}

