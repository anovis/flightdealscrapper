from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import DoesNotExist

import emailscrappers
import datetime

def my_handler(event, context):
    time = datetime.datetime.utcnow()
    timepicker = 3600 * ((time.hour -5) % 24 +1)

    city_group_dict = {}
    for user in User.rate_limited_scan(read_capacity_to_consume_per_second=4,filter_condition=User.time == timepicker):
        if city_group_dict.get(user.city, False):
            city_group_dict[user.city].append(user.email)
        else:
            city_group_dict[user.city] = [user.email]

    for city, email_list in city_group_dict.items():
        try:
            cached_flight = FlightCache.get(city)
                return {'deals': cached_flight.deals,'hrefs':cached_flight.hrefs}
        except DoesNotExist:
            print(city)
            print("not cached")


    response = DYNAMO.scan(TableName=DYNAMO_TABLE,ExpressionAttributeValues={':lambdatime': {'N': str(timepicker),},},FilterExpression='#t=:lambdatime',ExpressionAttributeNames={"#t" : "time"},ProjectionExpression="city, email")
    items = response['Items']
    for person in items:
        to = person['email']['S']
        x = emailscrappers.TheFlightDeal(person['city']['S'])
        y = emailscrappers.SecretFlying(person['city']['S'])
        e = emailscrappers.EmailScraper(person['city']['S'], to, [x, y])
        e.send_email()

    return


class User(Model):
    """
    dailyflightdeals
    """
    class Meta:
        table_name = "dailyflightdeals"
    email = UnicodeAttribute(hash_key=True)
    city = UnicodeAttribute(range_key=True)
    time = NumberAttribute()

class FlightCache(Model):
    """
    cached_flights
    """
    class Meta:
        table_name = "cached_flights"
    city = UnicodeAttribute(hash_key=True)
    time = UTCDateTimeAttribute()
    deals = ListAttribute()
    hrefs = ListAttribute()