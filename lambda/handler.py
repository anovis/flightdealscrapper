import boto3
import emailscrappers
import datetime
DYNAMO = boto3.client('dynamodb')
DYNAMO_TABLE = "dailyflightdeals"

def my_handler(event, context):
    time = datetime.datetime.utcnow()
    timepicker = 3600 * ((time.hour -5) % 24 +1)
    response = DYNAMO.scan(TableName=DYNAMO_TABLE,ExpressionAttributeValues={':lambdatime': {'N': str(timepicker),},},FilterExpression='#t=:lambdatime',ExpressionAttributeNames={"#t" : "time"},ProjectionExpression="city, email")
    items = response['Items']
    for person in items:
        to = person['email']['S']
        x = emailscrappers.TheFlightDeal(person['city']['S'])
        y = emailscrappers.SecretFlying(person['city']['S'])
        e = emailscrappers.EmailScraper(person['city']['S'], to, [x, y])
        e.send_email()

    return