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
driver.get(' https://www.target.com/')

# Click on SignIn Button
# Sign_in = //a[@data-test='@web/AccountLink']
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
# wait for 4 sec
sleep(2)
# Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(2)

# Verify SignIn page opened:
# $x("//h1[contains(span,'Sign into your Target account')]")
required_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1[contains(span,'Sign into your Target account')]").text
print(actual_text)

sign_in_button = driver.find_element(By.XPATH, "//button[contains(span,'Sign in with password')]")
print(f"Sign In Button is visible with this text on it {sign_in_button.text}")

assert actual_text == required_text, f"Sign In page is incorrect with this text on it {sign_in_button}"
print('Success , we are on right page!!')

driver.quit()
