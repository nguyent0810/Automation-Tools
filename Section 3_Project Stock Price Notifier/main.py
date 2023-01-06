import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.implicitly_wait(30)
    return driver

def clean_percentage(percentage):
    if "+" in percentage:
        percent = percentage.replace("+",'')
    percent = percent.split("%")[0]
    return float(percent)

def send_email():
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = ""
    receiver_email = ""
    message = """\
        Subject: Hi there
        The percentage is under -10%"""
    password = input("Type email password: ")

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()

def stock_price_notifier():
    driver = get_driver()
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    time.sleep(5)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    origin_percentage = soup.find('span', class_='stock-trend').get_text()
    percentage = clean_percentage(origin_percentage)
    if percentage < -0.10:
        send_email()
    else: 
        print(f"The percentage now is {per}")
    return percentage

stock_price_notifier()
