import smtplib, logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

LOGGER = logging.getLogger('Notify')

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env') # container path
GMAIL_APPLICATION_TOKEN         = str(os.environ.get('GMAIL_APPLICATION_TOKEN'))
SENDER_GMAIL                    = str(os.environ.get('SENDER_GMAIL'))

def notify(useremail='', message=''):
    gmail_content = MIMEMultipart()

    gmail_content["subject"] = '[INFO] DL Home Running'
    gmail_content["from"] = SENDER_GMAIL
    gmail_content["to"] = useremail
    gmail_content.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(SENDER_GMAIL, GMAIL_APPLICATION_TOKEN)
            LOGGER.info('sending email')
            smtp.send_message(gmail_content)
        except:
            raise ValueError('send failed')