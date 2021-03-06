import React, { Component } from 'react';
import { Button, Alert } from 'react-bootstrap';
var Spinner = require('react-spinkit');
var axios = require('axios');


const alert = <Alert bsStyle="warning" >
                            <h4>No Deals Found!</h4>
                            <p>Try again with a different city or at a later time</p>
                          </Alert>



export default class Selection extends React.Component {
  constructor(props) {
    super(props);
    this.state = {city: '',deals:[], hrefs:[], loading: false, nodeals: false};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({city: event.target.value});
  }

  handleSubmit(event) {
    this.setState({loading: true})
    axios.get('https://woysf8pmu6.execute-api.us-east-1.amazonaws.com/api/citydeals/' + this.state.city)
        .then((response) => {
          if (response.data.deals.length ==0){
            this.setState({nodeals:true})
            }
          else{
            this.setState({nodeals:false})
            }
          this.setState({deals: response.data.deals, hrefs:response.data.hrefs,loading: false, skipinit: true})
        })
        .catch((error) => {console.log(error)})
    event.preventDefault();
  }

  render() {
    var selection_list = [];
      for (var i=0; i < this.state.deals.length; i++){
          selection_list.push(<li className="li-sub"><a className="li-sub-a" href={this.state.hrefs[i]}> {this.state.deals[i]} </a></li>)
      }

    return (

    <div>
      <form onSubmit={this.handleSubmit}>
        <div>
          <label>See Latest Flight Deals from any City</label>
          <input type="city" className="form-styling" id="city" value={this.state.city} onChange={this.handleChange} placeholder="City Name" />
        </div>
         <input type="submit" value="Submit" className="btn btn-default" />
      </form>
       <ul className="ul-sub">
        {selection_list}
       </ul>
       {this.state.loading && <Spinner name='three-bounce' color='blue'/> }
       <div class="padding-top">
       {this.state.nodeals && alert}
            </div>
              </div>
    );
  }
}

