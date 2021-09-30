#!/usr/bin/python3

# You must call this file with an address that you want to send the message to.
# For example: python3 palsign.py example@example.com
    
# from typing import Text
import yaml
import urllib.request
import re
import smtplib
import sys

url = 'https://www.palsweb.com/thought-for-the-day'
with urllib.request.urlopen(url) as res:
    html = res.read().decode("utf-8")

date = re.search(r'("thought-date">)(.+)(<)', html)
thought = re.search(r'("thought">)(.+)(<)', html)

def msg():
    message0 = 'Subject:Thought For the Day'
    message1 = '% s ' % (date.group(2))
    message2 = '% s ' % (thought.group(2))
    message3 = 'Brought to you by the Pal\'s website.'
    return (message0 + '\n' + message1 + '\n' + message2 + '\n\n' + message3)

# print(msg()) # Uncomment for debugging

# Parameters (some of which are in a .yaml file stored separately).
conf = yaml.load(open('./mail_sanitized.yaml'), Loader=yaml.BaseLoader)
email = conf['user']['email']
pwd = conf['user']['password']
phone = sys.argv[1]
message = msg()

# For sending text message. May hide this information in a separate file.
def notifyEmail():
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(email, pwd)
        server.sendmail(email, phone, message)
        server.close()
        print('Email sent to: '+ phone)
    except:
        print('Something went wrong.')
# End email to text info

notifyEmail()
