import React, { Component } from 'react';
import TimePicker from 'react-bootstrap-time-picker';
import { ControlLabel,Form,Button,FormGroup,FormControl,Col,Checkbox } from 'react-bootstrap';
var axios = require('axios');

export default class Signup extends React.Component {
  constructor() {
    super();

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

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

   handleSubmit(event) {
    event.preventDefault();
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
      <Form horizontal onSubmit={this.handleSubmit}>
        <FormGroup controlId="formHorizontalEmail">
          <Col componentClass={ControlLabel} sm={2}>
            Email
          </Col>
          <Col sm={10}>
            <FormControl onChange={this.handleChange} value={this.state.email} name="email" type="email" placeholder="Email" />
          </Col>
        </FormGroup>
         <FormGroup controlId="formHorizontalEmail">
                  <Col componentClass={ControlLabel} sm={2}>
                    City
                  </Col>
                  <Col sm={10}>
                    <FormControl onChange={this.handleChange} value={this.state.city} name="city" type="city" placeholder="City" />
                  </Col>
         </FormGroup>

        <FormGroup controlId="formHorizontalPassword">
          <Col componentClass={ControlLabel} sm={2}>
            Time
          </Col>
             <TimePicker onChange={this.handleChange} value={this.state.time} name="time "/>
        </FormGroup>

        <FormGroup>
          <Col smOffset={2} sm={10}>
            <Checkbox>Remember me</Checkbox>
          </Col>
        </FormGroup>

        <FormGroup>
          <Col smOffset={2} sm={10}>
            <Button type="submit">
              Sign Up
            </Button>
          </Col>
        </FormGroup>
      </Form>
      );
  }
}