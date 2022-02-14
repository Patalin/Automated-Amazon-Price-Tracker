# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this
import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = 'https://www.amazon.com/Apple-AirPods-3rd-Generation-Renewed/dp/B09M94KXPN/ref=sr_1_15?crid=' \
              '3PVXUMJXHIH0&keywords=airpods&qid=1644837391&sprefix=airpods%2Caps%2C162&sr=8-15 '
MY_EMAIL = 'send_from_your_email@email.com'
MY_PASS = 'your_password'
SEND_TO_EMAIL = 'send_to_any_email'
PRICE_TO_BUY = 150

response = requests.get(PRODUCT_URL, headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                 '(KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'})

# Parse the data from the website
web_page_data = response.text
soup = BeautifulSoup(web_page_data, 'lxml')

# Find the price in website
price = soup.find(name='span', class_='a-offscreen')
product_title = soup.find(name='span', class_='a-size-large product-title-word-break').string.replace('  ', '')

# Transform the string '$139.95' in float 139.95
float_price = float(price.string.replace('$', ''))

print(float_price)
print(product_title)

# If the price of the product < $150, send mail alert
if float_price < PRICE_TO_BUY:
    money_saved = int(PRICE_TO_BUY - float_price)
    subject_email = f'Subject:Amazon Price Alert!\n\nYour price target is: ${PRICE_TO_BUY}\n\n {product_title} ' \
                    f'is now ${float_price}\n\nYou can save: ${money_saved} \n\nBuy it now from: \n\n{PRODUCT_URL}'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=SEND_TO_EMAIL,
                            msg=subject_email)