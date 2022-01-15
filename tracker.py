from genericpath import commonprefix
import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import smtplib
import time

def check_price():
    URL = input("Enter Link of Cryptocurrency you want to track: ")
    
    target = input("Enter Target Price: ")

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find("div", {"class": "priceValue"}).get_text()
    name = soup.find("span", {"class": "sc-1eb5slv-0 sc-1308828-0 bwAAhr"}).get_text()

    converted_price = Decimal(sub(r'[^\d.]', '', price))

    if(converted_price < float(target)):
        send_email()
        return False
    else:
        return True

def send_email():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.starttls
    server.ehlo()

    server.login('thejonathancao@gmail.com', 'PASSWORD')
    
    subject = 'PRICE DOWN! BUY NOW!'
    body = 'Please go on your exchange and scoop up as much as possible!'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'thejonathancao@gmail.com',
        'jonathancao2@outlook.com',
        msg
    )
    print('Alert Succesfully Sent!')
    
    server.quit()

while(True):
    check_price()



