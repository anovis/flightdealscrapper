import React, { Component } from 'react';
import TimePicker from 'react-bootstrap-time-picker';
import { ControlLabel,Form,Button,FormGroup,FormControl,Col,Checkbox } from 'react-bootstrap';
var axios = require('axios');

export default class Signup extends React.Component {
  constructor() {
    super();

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleTime = this.handleTime.bind(this);

    this.state = { time: 0,city:"",email:"" };
  }

  handleChange(e) {   // <- prints "3600" if "01:00" is picked
    if (e.target){
        var update={}
        update[e.target.name] = e.target.value;
        console.log(this.state)
        this.setState(update);
      }
  }
  handleTime(newtime){
  this.setState({time:newtime});
  }



   handleSubmit(event) {
    //event.preventDefault();
    var headers = {
               'Access-Control-Allow-Methods': 'POST',
               'Access-Control-Allow-Headers': 'Content-Type, Authorization',
               'Access-Control-Allow-Origin':  'http://127.0.0.1:5000'
           }

    axios.post('http://127.0.0.1:5000/citydeals/newuser', this.state, headers)
          .then((response) => {
            console.log(response)})
          .catch((error) => {console.log(error)})


    }

  render() {
    return (
      <Form onSubmit={this.handleSubmit}>
            <label> Email </label>
            <input className="form-styling" onChange={this.handleChange} value={this.state.email} name="email" type="email" placeholder="Email" />

            <label> City </label>
            <input className="form-styling" onChange={this.handleChange} value={this.state.city} name="city" type="city" placeholder="City" />

           <label> Time </label>
           <div className="fix-time"> </div> <TimePicker className="form-styling" onChange={this.handleTime} value={this.state.time} type="time" name="time "/>

           <input type="submit" value="Submit" className="btn btn-default" />
      </Form>
      );
  }
}