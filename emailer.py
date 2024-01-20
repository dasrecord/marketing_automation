import smtplib
import csv
import time
import configparser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_contacts(filename):
    names, emails = [], []
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            names.append(row[1])
            emails.append(row[9])
    return names, emails

def get_message(filename):
    with open(filename, 'r') as file:
        return file.read()

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Email settings
MY_ADDRESS = config.get('Email', 'MY_ADDRESS')
PASSWORD = config.get('Email', 'PASSWORD')

# Email sending settings
BUFFER = 60  # The delay (in seconds) between each email. Adjust as needed to avoid being flagged for spamming.

# SMTP settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  
names, emails = get_contacts('msj_leads.csv') # remember to include the path to your csv contact file
message_template = get_message('message.html') # remember to edit the message file to include your own message

s = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

for name, email in zip(names, emails):
    msg = MIMEMultipart()
    message = message_template.replace('PERSON_NAME', name)
    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "This is a test" # Change this to your own subject
    msg.attach(MIMEText(message, 'html'))  # 'html' indicates that the email content is HTML
    s.send_message(msg)
    time.sleep(BUFFER)
    print(f"Email sent to {name} at {email}")
s.quit()