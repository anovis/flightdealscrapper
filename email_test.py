
import smtplib
s = smtplib.SMTP(host="smtp.gmail.com", port = "587")
s.starttls()
s.login('manwei.test@gmail.com','testing123')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart() #create the message
msg['From'] = 'manwei.test@gmail.com'
msg['To'] = 'manwei.chan@gmail.com'
msg['Subject'] = "This is a TEST"
msg.attach(MIMEText('test','plain'))
s.send_message(msg)