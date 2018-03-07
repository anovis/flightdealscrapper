import emailscrappers

to = "austen.novis@gmail.com"
x = emailscrappers.TheFlightDeal("Washington")
y = emailscrappers.SecretFlying("Washington")
e = emailscrappers.EmailScraper("Washington", to, [x, y])
e.send_email()
