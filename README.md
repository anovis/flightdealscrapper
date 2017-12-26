# flightdealscrapper

### Flight Email Scrapper

* base flight classes are in emailscrappers
* each parser is its own class (see Secretflying and TheFLightDeal as examples)
* flight_email.py has working example on how to scrape and send emails using the new classes

### Frontend

* The frontend is written in React
* The index.js calls App.js which will contain all the necessary components. Create each new component separately and
import into App.js
* To run the frontend go into react-flightscrapper folder and run `npm start`

* The react build file is uploaded to S3 and hosted there

### Backend

* The backend is written in Python using Chalice
* Chalice uploads all functions to AWS API gateway and creates corresponding lambdas's
