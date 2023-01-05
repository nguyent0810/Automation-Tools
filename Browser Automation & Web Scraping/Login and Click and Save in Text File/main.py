from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.implicitly_wait(30)

    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    return text.split(": ")[1]
def save_text_file(text):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d.%H-%M-%S")
    with open(f"{dt_string}.txt", 'w') as f:
        f.write(text)
def main():
    driver = get_driver()
    driver.find_element(By.ID, "id_username").send_keys("automated")
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element(By.CSS_SELECTOR, "a[class$='navbar-brand']").click()
    element = driver.find_element(By.CSS_SELECTOR, 'div[class="text-success"]')
    save_text_file(clean_text(element.text))

print(main())
