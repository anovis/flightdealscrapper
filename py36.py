import smtplib
s = smtplib.SMTP(host="smtp.gmail.com", port = "587")
s.starttls()
s.login('manwei.test@gmail.com','testing123')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.request import urlopen
from urllib.request import Request
import html.parser
from html.parser import HTMLParser

flist = []
plist = []
llist = []
flist2 = []
llist2 = []

def send_email(city):
    
    data_message = ""
    
    #secret flying
    parser = SecretFlyingParser()
    res = urlopen('http://www.secretflying.com/usa-deals/')
    html = str(res.read(), res.headers.get_content_charset('utf8'))
    parser.feed(html)
    
    parser2 = SecretFlyingParser()
    res = urlopen('http://www.secretflying.com/usa-deals/')
    html = str(res.read(), res.headers.get_content_charset('utf8'))
    parser2.feed(html)
    
    flightW = filter(lambda x: "Boston" in x, flist)
    #the flight deal
    parser3 = FlightDealParser()
    
    site = 'http://www.theflightdeal.com/'
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    
    req= Request(site,headers=hdr)
    res = urlopen(req)
    html = str(res.read(), res.headers.get_content_charset('utf8'))
    parser3.feed(html)

    for f in flightW:
        data_message = data_message + '<h3>' + f + '</h3>'    
        
    
    for l in list(set(llist)):
        data_message = data_message + "<br><a href=" + l + "/>" + l + "</a>"
     
    for f in flist2:
        data_message = data_message + '<h3>' + f + '</h3>'    
    
    for l in list(set(llist2)):
        data_message = data_message + "<br><a href=" + l + "/>" + l + "</a>"
    

    msg = MIMEMultipart() #create the message
    msg['From'] = 'manwei.test@gmail.com'
    msg['To'] = 'austen.novis@gmail.com'
    msg['Subject'] = "This is a TEST"
    msg.attach(MIMEText(data_message,'html'))
    s.send_message(msg)
    print("sent email?")

    return 'Worked'
    
    
class SecretFlyingParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'rel' and value == 'bookmark':
                    href, link = attrs[0]
                    if 'boston' in link:
                        llist.append(link)

                        
    def handle_data(self, data):
        if ((len(data) > 45) & (len(data) < 150)): 
            #print "Encountered some data  :", data
            #print len(data)
            addflight(data)
            
            
class FlightDealParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'rel' and value == 'bookmark':
                    href, link = attrs[0]
                    title, deal = attrs[2]
                    if 'boston' in link:
                        llist2.append(link)
                        flist2.append(deal)



def addflight(flight):
    if ('/') not in flight:
        if ('signup') not in flight:
            if 'USA Flight Deals - Secret Flying' not in flight:
                if 'adsbygoogle' not in flight:
                    if '@' not in flight:
                        if '#' not in flight:
                            price = flight[flight.find('$')+1:flight.find('$')+4]
                            if price not in plist:
                                flist.append(flight)
                                plist.append(price)
    return

send_email('xxxx')
