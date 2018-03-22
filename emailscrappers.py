from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.request import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
secret = 'secret'

class EmailScraper:
    def __init__(self, city, subscribers, scrappers):
        self.city = city
        self.scrappers = scrappers
        self.subscribers = subscribers
        self.deal_list = []
        self.email_client = self.create_email_client
        self.msg = self.create_message()

    @property
    def create_email_client(self):
        s = smtplib.SMTP(host="smtp.gmail.com", port = "587")
        s.starttls()
        s.login('dailyflightdeals@gmail.com',secret)
        return s

    def create_message(self):
        msg = MIMEMultipart()
        msg['From'] = 'dailyflightdeals@gmail.com'
        msg['BCC'] = self.subscribers
        msg['Subject'] = "Daily Flights from " + self.city
        msg.attach(MIMEText(self.list_to_html(), 'html'))
        return msg

    def scrapper_deal_list(self):
        for scrapper in self.scrappers:
            self.deal_list = self.deal_list + scrapper.parse_soup()

    def list_to_html(self):
        mess_body = "<h2> Today's Flight Deals from " + self.city + "</h2>"
        self.scrapper_deal_list()
        for deal in self.deal_list:
            mess_body = mess_body + "<br><h3><a href=\"" + deal["href"] + "\" >" + deal["title"] + "</a></h3>"
        return mess_body

    def send_email(self):
        if self.deal_list:
            self.email_client.send_message(self.msg)


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
        #return list of deals
        pass


class SecretFlying(BaseScrapper):
    def __init__ (self, city):
        self.website = "http://www.secretflying.com/usa-deals/"
        BaseScrapper.__init__(self, city)

    def open_url(self):
        return urlopen(self.website)

    def parse_soup(self):
        deal_list = self.soup.find_all(title=re.compile('.*' + self.city), text=True, class_=None)
        return deal_list


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
        deal_list = self.soup.find_all(title=re.compile('.*' + self.city),text=True,class_=None)
        return deal_list

