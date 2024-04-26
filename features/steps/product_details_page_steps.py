from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ADD_CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Add to cart for Taylors of Harrogate Yorkshire - 160ct']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
COLOR_OPTION = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")


@then("Click on Add to cart button")
def add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@then('Store product name')
def store_product_name(context):
    product_name = context.app.base_page.get_text_from_element(*SIDE_NAV_PRODUCT_NAME)


@given('Open target product {product_id} page')
def open_target_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through {product_name} colors')
def click_product_and_verify_colors(context, product_name):
    expected_colors = {
        "A-91511634": ['dark khaki', 'black/gum', 'stone/grey', 'white/gum'],
        "A-54551690": ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    }
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTION)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors[product_name] == actual_colors, (f'Expected {expected_colors[product_name]} did not match '
                                                            f'actual {actual_colors}')
