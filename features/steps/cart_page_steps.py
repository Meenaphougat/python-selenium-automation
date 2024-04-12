from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")
TOTAL_PRICE = (By.CSS_SELECTOR, "span[class*='styles__CartSummarySpan-sc-odscpb-3']")


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    print(actual_text)
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")


@then("Verify Item is visible in cart")
def verify_item_visible(context):
    visible_item = context.driver.find_element(*TOTAL_PRICE).text
    print(visible_item)
    expected_item = '$10.99 subtotal1 item'
    assert expected_item == visible_item, f'Expected {expected_item}, but got {visible_item}'
