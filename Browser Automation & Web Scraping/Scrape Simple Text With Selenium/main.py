from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


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

    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = text.split(": ")[1]
    return output

def main():
    driver = get_driver()
    element = driver.find_element(By.CSS_SELECTOR,"h1[id$='displaytimer'] > div")
    return clean_text(element.text)

print(main())