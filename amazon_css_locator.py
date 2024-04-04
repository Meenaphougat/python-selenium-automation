from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get(' https://www.amazon.com')
# SignIn Click search by class
sleep(1)
driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()
sleep(4)
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "a[href='/ref=ap_frn_logo']")
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "#ap_email")
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "#continue")
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")
driver.quit()