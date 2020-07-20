import time
import sys
import smtplib
import os
from getpass import getpass
from shutil import copyfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

hostedDomain = sys.argv[1]


removeSpaces = lambda inputstr: inputstr.replace(" ", "")

senderEmail = str(input("Enter sender email: "))
senderEmailPassword = str(getpass("Enter sender password: "))


try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(senderEmail, senderEmailPassword)
except:
    raise Exception("Incorrect Email, Password combination.")

recipientEmail = str(input("Enter recipient email: "))
emailSubject = str(input("Enter email subject: "))
emailSubjectRemoved = removeSpaces(emailSubject)
emailName = recipientEmail + emailSubjectRemoved

message = str(input("Enter email body: "))
source = "{}/images/{}".format(hostedDomain, emailName)

msg = MIMEMultipart("alternative")

msg["Subject"] = emailSubject
msg["From"] = senderEmail
msg["To"] = recipientEmail

html = '''
<html>
  <head></head>
  <body>
    <p>{}</p>
    <img src='{}' width="1", height="1">
  </body>
</html>
'''
html = html.format(message, source)

content = MIMEText(html, 'html')
msg.attach(content)

server.sendmail(senderEmail, recipientEmail, msg.as_string())
server.quit()

time.sleep(5)

copyfile(
    "{}/images/main.png".format(os.getcwd()),
    "{}/images/{}.png".format(os.getcwd(), emailName),
)
