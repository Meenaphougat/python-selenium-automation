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
driver.find_element(By.XPATH, "//span[@class='nav-line-2 ']").click()
# Search by label
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# Search by ID
driver.find_element(By.ID, value="ap_email").click()
# Search for Continue button
driver.find_element(By.ID, value="continue")
# Search for Conditions of use link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref"
                              "=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# Search for Privacy Notice link by text
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
# Need Help drop down
driver.find_element(By.XPATH, "//a[@href='javascript:void(0)']").click()
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# Search Other issues with ID
driver.find_element(By.ID, "ap-other-signin-issues-link")
# Search button  Continue by ID
driver.find_element(By.ID, "createAccountSubmit").click()

sleep(2)
driver.quit()
