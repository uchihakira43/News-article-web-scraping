import smtplib
import datetime, time, os
td = datetime.date.today()

from requests_html import HTMLSession
session = HTMLSession()
url = 'https://news.google.com/home?hl=en-CA&gl=CA&ceid=CA:en'

r = session.get(url)
#opens up chrome in the background
r.html.render(sleep=1, scrolldown=1)

articles = r.html.find('article')

newslist = []

for item in articles:
    try:
        newsitem = item.find('h4', first=True)
        newsarticle = {
        'Title' : newsitem.text,
        'Link' : newsitem.absolute_links, #gives the full link not just the part after the slash
        'Date' : td.strftime("%b-%d-%Y")
        }
        newslist.append(newsarticle)
    except:
        pass

#print((newslist)[1]) #prints index position of title and links

#Email login requirements
gmail_user = 'uchihakira40@gmail.com'
gmail_app_password = 'iwkp fqgt syzb xpnx'

sent_from = gmail_user
sent_to = ['uchihakira40@gmail.com', 'uchihakira40@gmail.com']
sent_subject = " Hello ! Here are today's TOP news HEADLINES >>"
sent_body = str(newslist)


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)



