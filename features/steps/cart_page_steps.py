from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")
TOTAL_PRICE = (By.CSS_SELECTOR, "span[class*='styles__CartSummarySpan-sc-odscpb-3']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"
