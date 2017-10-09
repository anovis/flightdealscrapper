from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.request import Request

class BaseSite:
    def __init__(self, city):
        self.city = city
        self.res = self.open_url()
        self.soup = self.get_soup()

    def open_url(self):
        pass

    def get_soup(self):
        html = str(self.res.read(), self.res.headers.get_content_charset('utf8'))
        return BeautifulSoup(html,'html.parser')


class SecretFlying(BaseSite):
    def __init__ (self, city):
        self.websites = ["http://www.secretflying.com/usa-deals/","http://www.secretflying.com/usa-deals/page/2"]
        BaseSite.__init__(self, city)

    def open_url(self):
        return urlopen(self.websites[0])

    def print_name(self):
        print(self.soup.a)
        print(self.city)

x = SecretFlying("boston")
x.print_name()