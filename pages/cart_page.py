from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "")
    CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_cart_empty_message(self):
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        print(actual_text)
        expected_text = 'Your cart is empty'
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
        #self.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
