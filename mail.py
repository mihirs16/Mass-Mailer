import os
import smtplib
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv('.env')
EMAIL_ADDRESS = os.environ.get('SENDER_MAIL')
EMAIL_PASSWORD = os.environ.get('SENDER_PWD')
EMAIL_PORT = os.environ.get('SENDER_PORT')
EMAIL_SMTP = os.environ.get('SENDER_SMTP')

contacts = ['mihirs16@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts[0]

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL(EMAIL_SMTP, EMAIL_PORT) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)