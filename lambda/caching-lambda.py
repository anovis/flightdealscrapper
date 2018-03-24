import datetime
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.request import Request

# from pynamodb.models import Model
# from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute,UTCDateTimeAttribute
# from pynamodb.exceptions import DoesNotExist

city_caching = ["Washington", "New York", "San Francisco","Boston","Dallas","Atlanta" ]

def my_handler(event, context):
    time = datetime.datetime.utcnow()

    return time


# class FlightCache(Model):
#     """
#     cached_flights
#     """
#     class Meta:
#         table_name = "cached_flights"
#     city = UnicodeAttribute(hash_key=True)
#     time = UTCDateTimeAttribute()
#     deals = ListAttribute()
#     hrefs = ListAttribute()




def get_html():
    #Secret Flying

    website = "http://www.secretflying.com/usa-deals/"
    res = urlopen(website)
    html = str(res.read(),res.headers.get_content_charset('utf8'))
    secretBS = BeautifulSoup(html,'html.parser')

    #Flight Deal

    website = "http://www.theflightdeal.com/"
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    res = urlopen(Request(website,headers=hdr))
    html = str(res.read(),res.headers.get_content_charset('utf8'))
    flightBS = BeautifulSoup(html,'html.parser')

    return [secretBS, flightBS]

    #deal_list = self.soup.find_all(title=re.compile('.*' + self.city), text=True, class_=None)


html_list = get_html()
for city in city_caching:
    deal_list = []
    for html in html_list:
        deal_list =deal_list + html.find_all(title=re.compile('.*' + city), text=True, class_=None)
    print(deal_list)
