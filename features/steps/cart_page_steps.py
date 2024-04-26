from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_message()


@then('Verify cart has correct {item} product')
def verify_product_name(context, item):
    context.app.cart_page.verify_product_name(item)


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)
