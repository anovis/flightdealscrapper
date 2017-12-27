import { Alert, Button } from 'react-bootstrap';
import React, { Component } from 'react';


export default class Success extends React.Component {
  constructor(props) {
    super(props);
  }


  render() {
    return (
        <div class="padding-top">
            <Alert bsStyle="success" onDismiss={this.handleAlertDismiss} >
              <h4>Success!</h4>
              <p>You will begin getting deals shortly! Check out current flight deals under the <strong> Today's Deal </strong> tab'</p>
            </Alert>
        </div>
    );
  }
}

