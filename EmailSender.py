# go over to our gmail account and setup 2 factor authentication
# generate app password
# create a function to send the mail

import email
from email.message import EmailMessage
import EmailApp as ea
import ssl
import smtplib

sender_email = ea.fromEmail
sender_password = ea.password

receiver_email = ea.toEmail

subject = ea.subject

body = ea.body

# function
em = EmailMessage()
em['From'] = sender_email
em['To'] = receiver_email
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, receiver_email, em.as_string())