import emailscrappers
import re
# to = "austen.novis@gmail.com"
# x = emailscrappers.TheFlightDeal("Washington")
# y = emailscrappers.SecretFlying("Washington")
# e = emailscrappers.EmailScraper("Washington", to, [x, y])
# e.send_email()

x = emailscrappers.SecretFlying("Washington")
print(x.get_soup().find_all(title=re.compile('.*' + "Boston"), text=True, class_=None))