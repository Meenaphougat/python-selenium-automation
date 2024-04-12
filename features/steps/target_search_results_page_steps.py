from selenium.webdriver.common.by import By
from behave import then
from time import sleep

SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
PRODUCT_CLICK = (By.CSS_SELECTOR, "a[aria-label*='Taylors of Harrogate Yorkshire - 160ct']")


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'


@then('Click on product')
def click_on_product(context):
    context.driver.find_element(*PRODUCT_CLICK).click()
    sleep(4)
