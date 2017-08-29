import boto3
client = boto3.client('ses')
import urllib2
from HTMLParser import HTMLParser

flist = []
plist = []
llist = []
flist2 = []
llist2 = []

def lambda_handler(event, context):
    
    data_message = ""
    
    #secret flying
    parser = MyHTMLParser()
    res = urllib2.urlopen('http://www.secretflying.com/usa-deals/')
    html = unicode(res.read(), res.headers.getparam('charset'))
    parser.feed(html)
    res2 = urllib2.urlopen('http://www.secretflying.com/usa-deals/page/2')
    html2 = unicode(res2.read(), res.headers.getparam('charset')) 
    parser.feed(html2)
    res3 = urllib2.urlopen('http://www.secretflying.com/usa-deals/page/3')
    html3 = unicode(res3.read(), res.headers.getparam('charset')) 
    parser.feed(html3)
    flightW = filter(lambda x: "Boston" in x, flist)
    #the flight deal
    parser2 = MyHTMLParserFlightDeal()
    
    site = 'http://www.theflightdeal.com/'
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    
    req= urllib2.Request(site,headers=hdr)
    res = urllib2.urlopen(req)
    html = unicode(res.read(), res.headers.getparam('charset'))
    parser2.feed(html)

    for f in flightW:
        data_message = data_message + '<h3>' + f + '</h3>'    
        
    
    for l in list(set(llist)):
        data_message = data_message + "<br><a href=" + l + "/>" + l + "</a>"
     
    for f in flist2:
        data_message = data_message + '<h3>' + f + '</h3>'    
    
    for l in list(set(llist2)):
        data_message = data_message + "<br><a href=" + l + "/>" + l + "</a>"
    
    
    response = client.send_email(
    Source='dailyflightdeals@gmail.com',
    Destination={
        'ToAddresses': [
            'senan.ebrahim@gmail.com ',
        ]
    },
    Message={
        'Subject': {
            'Data': 'Todays Flight Deals'
        },
        'Body': {
            'Text': {
                'Data': data_message
            },
            'Html': {
                'Data': data_message
            }
        }
    }
    )
    
    return 'Worked'
    
    
class MyHTMLParser(HTMLParser):
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
        	
        	
class MyHTMLParserFlightDeal(HTMLParser):
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