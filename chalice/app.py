from chalice import Chalice
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.request import Request
import boto3
import json

DYNAMO = boto3.client('dynamodb')
DYNAMO_ARN = "dailyflightdeal"


app = Chalice(app_name="dailyflightdeal")
app.debug = True

@app.route('/citydeals/{city}',cors=True)
def get_deals(city):
    x = TheFlightDeal(city)
    y = SecretFlying(city)
    e = EmailScraper(city, "", [x, y])
    deals,hrefs = e.call_scrappers()
    return {'deals': deals,'hrefs':hrefs}

@app.route('/citydeals/newuser', methods=['POST'],cors=True)
def new_user():
    states= app.current_request.json_body
    response = DYNAMO.put_item(TableName=DYNAMO_ARN,Item={'email':{'S': states['email']},'city':{'S': states['city']},'time':{'N': str(states['time'])}})
    return response


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





