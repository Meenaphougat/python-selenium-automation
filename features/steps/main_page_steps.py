from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
# CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
TARGET_CIRCLE = (By.CSS_SELECTOR, "[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()


@when("Search for {item}")
def search_product(context, item):
    context.app.header.search_product(item)
    # context.wait.until(
    #     EC.invisibility_of_element_located(ADD_TO_CART_BTN),
    #     message=' Add to Cart button did not disappear'
    # )


@when('Click on Cart icon')
def click_cart(context):
    # context.driver.find_element(*CART_ICON).click()
    # context.wait.until(EC.element_to_be_clickable(CART_ICON)).click(),
    # message = ' Click on cart icon did not clickable'
    context.app.header.click_cart()

@when('Click on Target circle link')
def verify_target_circle(context):
    #sleep(6)
    context.wait.until(EC.element_to_be_clickable(TARGET_CIRCLE)).click(),
    message = ' Target circle did not clickable'


@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):  # expected_amount = '5'
    expected_amount = int(expected_amount)  # '5' (str) => 5 (int)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


