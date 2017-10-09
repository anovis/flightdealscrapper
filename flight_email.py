import parsers

to = "austen.novis@gmail.com"
x = parsers.TheFlightDeal("Boston")
y = parsers.SecretFlying("Boston")
e = parsers.EmailScraper("Boston",to,[x,y])
e.send_email()
