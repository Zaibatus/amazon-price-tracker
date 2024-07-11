import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

PRODUCT_URL = "https://www.amazon.com/dp/B075CWJ3T8?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
URL_HEADERS = {
    "User-Agent": "USER_AGENT",
    "Accept-Language": "ACCEPT_LANGUAGE",
    "Accept-Encoding": "ACCEPT_ENCODING"
}

# -------------------- Scraping Amazon product page ------------------------------- #

response = requests.get(PRODUCT_URL, headers=URL_HEADERS)
response.raise_for_status()
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")
# print(soup.prettify())

price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
price = float(f"{price_whole}{price_fraction}")
product_name = soup.find(name="span", id="productTitle").getText().encode('utf-8')

# -------------------- Sending email when price drop below a certain limit ------------------------------- #

price_threshold = 200

if price < price_threshold:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now €{price}\n{PRODUCT_URL}",
                            to_addrs=MY_EMAIL,
                            )




