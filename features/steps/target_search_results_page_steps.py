from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when
from time import sleep

SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
PRODUCT_CLICK = (By.CSS_SELECTOR, "[data-test='product-title']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
VIEW_CART_BUTTON = (By.CSS_SELECTOR, "[href='/cart']")


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    context.app.search_results_page.verify_search_results(expected_item)


@then('Verify that URL has {partial_url}')
def verify_search_page_url(context, partial_url):
    context.app.search_results_page.verify_partial_url(partial_url)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.base_page.wait_until_clickable(*SIDE_NAV_ADD_TO_CART_BTN)


@when("Click on View cart button to go inside Cart")
def view_cart_button(context):
    context.app.base_page.wait_until_clickable(*VIEW_CART_BUTTON)

