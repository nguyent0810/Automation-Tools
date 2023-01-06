from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    # options.add_argument("log-level=3")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.implicitly_wait(30)

    driver.get("https://www.titan22.com")
    return driver

def register_new_account(driver):

    driver.find_element(By.ID, "FirstName").send_keys("AutomationPython")
    driver.find_element(By.ID, "LastName").send_keys("AutomationPythonLastName")
    driver.find_element(By.ID, "Email").send_keys("AutomationPython@gmail.com")
    driver.find_element(By.ID, "CreatePassword").send_keys("11111111")
    driver.find_element(By.ID, "customer[accepts_terms]").click()
    driver.find_element(By.XPATH, "//button[text()='Create']").click()

def login_to_the_system(driver):
    driver.find_element(By.ID, "CustomerEmail").send_keys("AutomationPython@gmail.com")
    driver.find_element(By.ID, "CustomerPassword").send_keys("11111111")
    driver.find_element(By.XPATH, "//button[.='Sign In']").click()
    time.sleep(10000)


def main():
    driver = get_driver()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/account"]').click()
    # driver.find_element(By.CSS_SELECTOR, "div[class$='d-flex justify-content-between mt-2'] > a[href*='register']").click()
    # register_new_account(driver)
    login_to_the_system(driver)

main()
