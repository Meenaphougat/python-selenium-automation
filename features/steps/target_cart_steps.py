from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target(context):
    context.driver.get("https://www.target.com/")


@when("Click on Cart icon")
def click_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(6)


@then('Verify “Your cart is empty” message is shown')
def verify_cart_page(context):
    required_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH,
                                              "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']").text
    assert 'Your cart is empty' in actual_text, f'Error! You are not on right page {actual_text}'
    print(f'You are on right page and {actual_text}')

#
# print('Success , we are on right page!!')
