import React, { Component } from 'react';
import TimePicker from 'react-bootstrap-time-picker';
import { ControlLabel,Form,Button,FormGroup,FormControl,Col,Checkbox } from 'react-bootstrap';
import Success from './Success.js'
var axios = require('axios');


export default class Signup extends React.Component {
  constructor() {
    super();

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleTime = this.handleTime.bind(this);

    this.state = { time: 0,city:"",email:"", SuccessVisible: false};
  }

  handleChange(e) {   // <- prints "3600" if "01:00" is picked
    if (e.target){
        var update={}
        update[e.target.name] = e.target.value;
        this.setState(update);
      }
  }
  handleTime(newtime){
  this.setState({time:newtime});
  }



   handleSubmit(event) {
    event.preventDefault();
    var headers = {
               'Access-Control-Allow-Methods': 'POST',
               'Access-Control-Allow-Headers': 'Content-Type, Authorization',
               'Access-Control-Allow-Origin':  'http://flightdealbuilds.s3-website-us-east-1.amazonaws.com/build-1120/build',
               'Content-Type':'application/json'
           }

    axios.post('https://woysf8pmu6.execute-api.us-east-1.amazonaws.com/api/citydeals/newuser', this.state, headers)
          .then((response) => {
            if (response.data.len >= 1)
             {this.setState({SuccessVisible: true})}


             })
          .catch((error) => {console.log(error)})

    }

  render() {
    return (
    <div>
      <Form onSubmit={this.handleSubmit}>
            <label> Email </label>
            <input className="form-styling" onChange={this.handleChange} value={this.state.email} name="email" type="email" placeholder="Email" />

            <label> City that you want deals from (Major cities work best) </label>
            <input className="form-styling" onChange={this.handleChange} value={this.state.city} name="city" type="city" placeholder="City" />

           <label> Time when you would like to be emailed everyday if there are deals </label>
           <center><TimePicker className="form-styling" step={60} onChange={this.handleTime} value={this.state.time} type="time" name="time "/></center>

           <input type="submit" value="Submit" className="btn btn-default" />
      </Form>
        {this.state.SuccessVisible && <Success /> }
        </div>
      );
  }
}