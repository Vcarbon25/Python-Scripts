import smtplib, ssl #native modules
#from constants import Sender_email, password
#Outlook
port = 587 #This is the port to use the outlook server
smtp_server = "smtp.office365.com"
sender_email = sender_email
password = password
"""
Gmail
smtp_server = "smtp.gmail.com
port =465
password = Generate an app password in the account
Yahoo
smtp_server = "smtp.mail.yahoo.com
port =465 or 587
password = Generate an app password in the account

"""
receiver_email ="target@provider.com"
message="""
Subject: Email's title

Message body goes here."""
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    try:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password) # after this is already logged in the account
        server.sendmail(sender_email,receiver_email, message)
        print("Email send")
    


