#!/usr/bin/env python


import smtplib
import yaml

"""
Gmail sender. This acctually works
Just need to create an App password in Google Account
"""

CFG = yaml.load(open('cfg.yml', 'r'))

gmail_user = CFG['smtp']['user']
gmail_pwd =  CFG['smtp']['pass']
gmail_host =  CFG['smtp']['host']
gmail_port =  CFG['smtp']['port']

def send_email(sender, to_list, subject, content):

    

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (sender, ", ".join(to_list), subject, content)
    try:
        #server = smtplib.SMTP(SERVER)
        # or port 465 doesn't seem to work!
        server = smtplib.SMTP(gmail_host, gmail_port)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(sender, to_list, message)
        # server.quit()
        server.close()
        print 'Successfully sent the mail to', ", ".join(to_list)
    except Exception, e:
        print e

def main():
    sender = gmail_user
    to_list = [sender]
    subject = "Testing sending using gmail"
    content = "Testing sending mail using gmail servers"
    send_email(sender,to_list,subject,content)

if __name__ == '__main__':
    main()
