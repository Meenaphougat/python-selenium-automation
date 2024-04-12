from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#ADD_CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Add to cart for Pure Leaf Lemon Iced Tea - 6pk/16.9oz Bottles']")
ADD_CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Add to cart for Taylors of Harrogate Yorkshire - 160ct']")

VIEW_CART_BUTTON = (By.CSS_SELECTOR, "[href='/cart']")


@then("Click on Add to cart button")
def add_to_cart_button(context):
    context.driver.find_element(*ADD_CART_BUTTON).click()


@when("Click on View cart button to go inside Cart")
def view_cart_button(context):
    context.driver.find_element(*VIEW_CART_BUTTON).click()