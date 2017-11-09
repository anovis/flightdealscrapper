import { ListGroup,ListGroupItem } from 'react-bootstrap';
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
        subscription_list.push(<ListGroupItem> {this.state.subscriptions[i]} </ListGroupItem>)
    }

    return (
    <div>
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <label>Enter Email address you used to sign up</label>
              <input type="email" className="form-control" id="email" value={this.state.email} onChange={this.handleChange} placeholder="Email" />
             <input type="submit" value="Submit" className="btn btn-default" />
            </div>
                <div/>
          </form>
          <div><ListGroup>
      {subscription_list}
      </ListGroup></div>
       </div>
    );
  }
}

