from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
SIGN_IN_BTN_SIDE_NAV = (By.XPATH, "//a[@data-test='accountNav-signIn']")
SIGN_IN_TEXT = (By.XPATH, "//h1[contains(span,'Sign into your Target account')]")

@when("Click on SignIn icon")
def click_signin(context):
    context.driver.find_element(*SIGN_IN_BTN).click()
    #sleep(6)
    context.wait.until(
        EC.visibility_of_element_located(SIGN_IN_BTN),
        message='Side nav, Sign IN  is not visible'
    )


@when("From right side navigation menu, click Sign In")
def click_inside(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    #sleep(3)
    context.wait.until(
        EC.visibility_of_element_located(SIGN_IN_TEXT),
        message='Sign In Page is not visible'
    )


@then('Verify “Sign into your Target account” message is shown')
def verify_signin_page(context):
    required_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(*SIGN_IN_TEXT).text
    sign_in_button = context.driver.find_element(By.XPATH, "//button[contains(span,'Sign in with password')]")
    print(f"Sign In Button is visible with this text on it {sign_in_button.text}")

    assert actual_text == required_text, f"Sign In page is incorrect with this text on it {sign_in_button}"
    print('Success , we are on right page!!')

#
# print('Success , we are on right page!!')
