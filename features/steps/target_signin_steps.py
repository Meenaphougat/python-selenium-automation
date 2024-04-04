from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.driver.get("https://www.target.com/")


@when("Click on SignIn icon")
def click_signin(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(6)


@when("From right side navigation menu, click Sign In")
def click_inside(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(3)


@then('Verify “Sign into your Target account” message is shown')
def verify_signin_page(context):
    required_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH,
                                              "//h1[contains(span,'Sign into your Target account')]").text
    sign_in_button = context.driver.find_element(By.XPATH, "//button[contains(span,'Sign in with password')]")
    print(f"Sign In Button is visible with this text on it {sign_in_button.text}")

    assert actual_text == required_text, f"Sign In page is incorrect with this text on it {sign_in_button}"
    print('Success , we are on right page!!')

#
# print('Success , we are on right page!!')
