from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# SIGN_IN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
# SIGN_IN_BTN_SIDE_NAV = (By.XPATH, "//a[@data-test='accountNav-signIn']")
SIGN_IN_TEXT = (By.XPATH, "//h1[contains(span,'Sign into your Target account')]")


@when("Click on SignIn icon")
def click_signin(context):
    context.app.header.click_signIn()


@when("From right side navigation menu, click Sign In")
def click_inside(context):
    context.app.side_menu.click_inside()


@then('Verify “Sign into your Target account” message is shown')
def verify_signin_page(context):
    required_text = 'Sign into your Target account'
    context.app.base_page.verify_text(required_text, *SIGN_IN_TEXT)
    print('Success , we are on right page!!')
