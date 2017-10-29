import React, { Component } from 'react';
import TimePicker from 'react-bootstrap-time-picker';
import { ControlLabel,Form,Button,FormGroup,FormControl,Col,Checkbox } from 'react-bootstrap';
var axios = require('axios');

export default class Signup extends React.Component {
  constructor() {
    super();

    this.handleTimeChange = this.handleTimeChange.bind(this);

    this.state = { time: 0 };
  }

  handleTimeChange(time) {
    console.log(time);     // <- prints "3600" if "01:00" is picked
    this.setState({ time });
  }

   handleSubmit(event) {
    var headers = {
               'Access-Control-Allow-Methods': 'POST',
               'Access-Control-Allow-Headers': 'Content-Type, Authorization',
               'Access-Control-Allow-Origin':  'http://127.0.0.1:5000'
           }
    axios.post('http://127.0.0.1:5000/citydeals/newuser', { firstName: event}, headers)
          .then((response) => {
            console.log(response)})
          .catch((error) => {console.log(error)})
    event.preventDefault();

    }

  render() {
    return (
      <Form horizontal onSubmit={this.handleSubmit}>
        <FormGroup controlId="formHorizontalEmail">
          <Col componentClass={ControlLabel} sm={2}>
            Email
          </Col>
          <Col sm={10}>
            <FormControl type="email" placeholder="Email" />
          </Col>
        </FormGroup>
         <FormGroup controlId="formHorizontalEmail">
                  <Col componentClass={ControlLabel} sm={2}>
                    City
                  </Col>
                  <Col sm={10}>
                    <FormControl type="city" placeholder="Citys" />
                  </Col>
         </FormGroup>

        <FormGroup controlId="formHorizontalPassword">
          <Col componentClass={ControlLabel} sm={2}>
            Time
          </Col>
             <TimePicker onChange={this.handleTimeChange} value={this.state.time} />
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