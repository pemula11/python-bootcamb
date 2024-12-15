# importing os module for environment variables
import os
from bs4 import BeautifulSoup
import lxml, requests, smtplib


import requests
# importing necessary functions from dotenv library
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv()

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
price_text = soup.find(name="span", class_="aok-offscreen").getText().split()[0]
price_as_float = float(price_text.split("$")[1])

# email smtp

TARGET_PRICE = 100

if price_as_float <= TARGET_PRICE:

    title = soup.find(name="span", id="productTitle").getText()
    message = f"{title}\n\n is on sale for: {str(price_as_float)}"

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        result = smtp.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        smtp.sendmail(
            from_addr=os.getenv("EMAIL_ADDRESS"),
            to_addrs=os.getenv("EMAIL_ADDRESS"),
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )