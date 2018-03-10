from chalice import Chalice
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.request import Request
import boto3
from boto3.dynamodb.conditions import Key, Attr

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.attributes import NumberAttribute

DYNAMO = boto3.client('dynamodb')
DYNAMO_TABLE = "dailyflightdeals"


app = Chalice(app_name="dailyflightdeal")
app.debug = True

@app.route('/citydeals/{city}',cors=True)
def get_deals(city):
    city = city.replace("%20", " ").title()
    x = TheFlightDeal(city)
    y = SecretFlying(city)
    e = EmailScraper(city, "", [x, y])
    deals,hrefs = e.call_scrappers()
    return {'deals': deals,'hrefs':hrefs}


@app.route('/citydeals/newuser', methods=['POST'],cors=True)
def new_user():
    states= app.current_request.json_body
    response = DYNAMO.put_item(TableName=DYNAMO_TABLE,Item={'email':{'S': states['email']},'city':{'S': states['city'].title()},'time':{'N': str(states['time'])}})
    return {'success': 'true'}


@app.route('/subscriptions/{email}',cors=True)
def get_subscriptions(email):
    response = DYNAMO.query(TableName=DYNAMO_TABLE,ExpressionAttributeValues={':email': {'S': email,},},KeyConditionExpression='email=:email',ProjectionExpression='city')
    items = response['Items']
    cities = []
    for city in items:
        cities.append(city['city']['S'])

    return cities


@app.route('/subscriptions/{email}', methods=['PUT'], cors=True)
def update_subscriptions(email):
    data = app.current_request.json_body
    new_time = data['time']
    city = data['city']
    user = User.get(email, city)
    user.time.set(new_time)
    user.refresh()

    return user


@app.route('/subscriptions/{email}', methods=['DELETE'], cors=True)
def cancel_subscriptions(email):
    data = app.current_request.json_body
    city = data['city']
    user = User.get(email, city)
    user.delete()

    return {'success': 'subscription canceled'}


class EmailScraper:
    def __init__(self, city, subscribers, scrappers):
        self.city = city
        self.scrappers = scrappers
        self.subscribers = subscribers

    def call_scrappers(self):
        deal_name_total = []
        deal_href_total = []
        for scrapper in self.scrappers:
            deal_name, deal_href = scrapper.parse_soup()
            deal_name_total.extend(deal_name)
            deal_href_total.extend(deal_href)
        return deal_name_total,deal_href_total



class BaseScrapper:
    def __init__(self, city):
        self.city = city
        self.res = self.open_url()
        self.soup = self.get_soup()

    def open_url(self):
        #return url_open
        pass

    def get_soup(self):
        html = str(self.res.read(), self.res.headers.get_content_charset('utf8'))
        return BeautifulSoup(html,'html.parser')

    def parse_soup(self):
        #return html string
        pass

class SecretFlying(BaseScrapper):
    def __init__ (self, city):
        self.website = "http://www.secretflying.com/usa-deals/"
        BaseScrapper.__init__(self, city)

    def open_url(self):
        return urlopen(self.website)

    def parse_soup(self):
        deal_name = []
        deal_href = []
        deal_list = self.soup.find_all(title=re.compile('.*' + self.city),text=True,class_=None)
        for deal in deal_list:
            deal_name.append(deal["title"])
            deal_href.append(deal["href"])
        return deal_name, deal_href

class TheFlightDeal(BaseScrapper):
    def __init__ (self, city):
        self.website = "http://www.theflightdeal.com/"
        BaseScrapper.__init__(self, city,)

    def open_url(self):
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        req= Request(self.website,headers=hdr)
        return urlopen(req)

    def parse_soup(self):
        deal_name = []
        deal_href = []
        deal_list = self.soup.find_all(title=re.compile('.*' + self.city),text=True,class_=None)
        for deal in deal_list:
            deal_name.append(deal["title"])
            deal_href.append(deal["href"])
        return deal_name, deal_href

class User(Model):
    """
    dailyflightdeals
    """
    class Meta:
        table_name = "dailyflightdeals"
    email = UnicodeAttribute(hash_key=True)
    city = UnicodeAttribute(range_key=True)
    time = NumberAttribute()



