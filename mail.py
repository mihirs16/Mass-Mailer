import os
import smtplib
import data
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv('.env')
EMAIL_ADDRESS = os.environ.get('SENDER_MAIL')
EMAIL_PASSWORD = os.environ.get('SENDER_PWD')
EMAIL_PORT = os.environ.get('SENDER_PORT')
EMAIL_SMTP = os.environ.get('SENDER_SMTP')

def send_emails(contacts, coupons):
    for contact, coupon in zip(contacts, coupons[:len(contacts)]):
        try:
            msg = MIMEMultipart()
            msg['Subject'] = 'Test Email [AUTO]'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = contact['email']

            body_content = """
            <!DOCTYPE html>
            <html>
                <body>
                    <h1 style="color:SlateGray;">This is a stylised test Email!</h1>
                    <h3 style="color:red;">{}<h3>
                </body>
            </html>
            """.format(coupon)
            msg.attach(MIMEText(body_content, 'html'))

            filename = contact['attachment']
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename=certificate.pdf",
            )

            msg.attach(part)
            text = msg.as_string()

            with smtplib.SMTP_SSL(EMAIL_SMTP, EMAIL_PORT) as smtp:
                print('Mailing to: ' + contact['email'], coupon)
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
        except:
            print('Couldn\'t send: ' + contact['email'], coupon)
        data.update_coupons([coupon])
        print('Mailed to: ' + contact['email'], coupon)

        
send_emails(data.load_contacts(attachments='certificates'), data.load_coupons())