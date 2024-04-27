from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# SIGN_IN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
# SIGN_IN_BTN_SIDE_NAV = (By.XPATH, "//a[@data-test='accountNav-signIn']")
SIGN_IN_TEXT = (By.XPATH, "//h1[contains(span,'Sign into your Target account')]")


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Click on Target terms and conditions link')
def click_t_c_link(context):
    context.app.sign_in_page.click_t_c_link()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.term_condition_page.verify_tc_opened()


#### Steps for Sign In Icon
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
