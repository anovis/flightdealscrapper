# flightdealscrapper

### Notes

* This is for lambda so only using basic libraries
* Currently just create new function for each city
* have to keep 5 min time limit in mind if it takes too long to scrape

### Variables that change

* Emails
* Cities 
* Potentially (specific sites) Currently just have secret flying and the daily flight deal


### Test function 

`
{
  "account": "123456789012",
  "region": "us-east-1",
  "detail": {},
  "detail-type": "Scheduled Event",
  "source": "aws.events",
  "time": "1970-01-01T00:00:00Z",
  "id": "cdc73f9d-aea9-11e3-9d5a-835b769c0d9c",
  "resources": [
    "arn:aws:events:us-east-1:123456789012:rule/my-schedule"
  ]
}
`

#### Future Steps

* Frontend Website (login, register, view current subscriptions, set times)
* Backend (handle frontend traffic, send emails at user times)
* Email (generic function that takes in city as input with list of websites to scrape and sends email to user)