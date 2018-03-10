import { ListGroup,ListGroupItem, Button,Alert,ButtonGroup,Glyphicon,Popover,OverlayTrigger } from 'react-bootstrap';
import React, { Component } from 'react';
var axios = require('axios');


export default class Subscriptions extends React.Component {
  constructor(props) {
    super(props);
    this.state = {email: '',
                  subscriptions: [],
                  noemails: false,
                  new_time:0};
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleTime = this.handleTime.bind(this);
    this.handleUpdate = this.handleUpdate.bind(this);
//    this.handleDelete = this.handleDelete.bind(this);
  }


  handleChange(event) {
    this.setState({email: event.target.value});
  }

  handleTime(event) {
      this.setState({time: event.target.value* 3600,new_time:event.target.value});
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

    handleDelete(e) {
      var headers = {
                   'Access-Control-Allow-Methods': 'POST',
                   'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                   'Access-Control-Allow-Origin':  'http://www.dailyflightdeal.com/',
                   'Content-Type':'application/json'
               }
      var num = e.currentTarget.value
      var subscription_to_delete = {'city':this.state.subscriptions[num]['city']}
      console.log(subscription_to_delete)
      axios.post('https://woysf8pmu6.execute-api.us-east-1.amazonaws.com/api/subscriptions/' + this.state.email, subscription_to_delete, headers)
          .then((response) => {
          var cur_array = this.state.subscriptions
          cur_array.splice(num,1)
          console.log(cur_array)
          this.setState({subscriptions:cur_array})
          })
          .catch((error) => {console.log(error)})
    }

   handleUpdateButton(event){
        this.setState({city: event.target.value});
    }

   handleUpdate(event) {
    //event.preventDefault();
    var headers = {
                      'Access-Control-Allow-Methods': 'PUT',
                      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                      'Access-Control-Allow-Origin':  'http://www.dailyflightdeal.com/',
                      'Content-Type':'application/json'
                  }

     axios.put('https://woysf8pmu6.execute-api.us-east-1.amazonaws.com/api/subscriptions/' + this.state.email,this.state, headers)
         .then((response) => {
          //time update
         })
         .catch((error) => {console.log(error)})

   }




  render() {
     const popoverBottom = (
         <Popover id="popover-positioned-bottom" title="Change Time">
                 <form onSubmit={this.handleUpdate}>
                   <div className="form-group">
                     <input className="form-styling" type="number" id="new_time" value={this.state.new_time} onChange={this.handleTime} placeholder="New Time" />
                   </div>
                    <input className="btn btn-default" type="submit" value="Submit" />

                 </form>
         </Popover>
         );
    var subscription_list = [];
    for (var i=0; i < this.state.subscriptions.length; i++){
        subscription_list.push(<li className="li-sub"><a className="li-sub-a"> {this.state.subscriptions[i]['city']} : {this.state.subscriptions[i]['time'] /3600 }
         <ButtonGroup className="right-align">
         <OverlayTrigger trigger="click" placement="bottom" overlay={popoverBottom}>
              <Button value={this.state.subscriptions[i]['city']} onClick={this.handleUpdateButton.bind(this)}>
                <Glyphicon  value={this.state.subscriptions[i]['city']} glyph="edit" />
              </Button>
         </OverlayTrigger>
              <Button value={[i]} onClick={this.handleDelete.bind(this)}>
                <Glyphicon value={[i]} glyph="trash" />
              </Button>
         </ButtonGroup>
              </a></li>)
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

