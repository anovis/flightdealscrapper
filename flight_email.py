import emailscrappers

to = "austen.novis@gmail.com"
x = emailscrappers.TheFlightDeal("Boston")
y = emailscrappers.SecretFlying("Boston")
e = emailscrappers.EmailScraper("Boston", to, [x, y])
e.send_email()
