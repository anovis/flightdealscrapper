import React, { Component } from 'react';
var axios = require('axios');

export default class Selection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {city: '',deals:"<div> </div>"};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({city: event.target.value});
  }

  handleSubmit(event) {
    axios.get('http://127.0.0.1:5000/citydeals/' + this.state.city)
        .then((response) => {
          this.setState({deals: response.data.deals})
        })
        .catch((error) => {console.log(error)})
    event.preventDefault();
  }

  render() {
    return (
    <div>
    <div className="col-md-4" />
      <form onSubmit={this.handleSubmit}>
        <div className="form-group col-md-4">
          <label>See Latest Flight Deals from any City</label>
          <input type="city" className="form-control" id="city" value={this.state.city} onChange={this.handleChange} placeholder="City Name" />
         <input type="submit" value="Submit" className="btn btn-default" />
        </div>
            <div className="col-md-4" />
      </form>
      <div className="col-md-4" />
       <div className="col-md-8" dangerouslySetInnerHTML={{__html: this.state.deals}} />
        <div className="col-md-2" />
       </div>
    );
  }
}

