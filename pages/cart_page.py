from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
    TOTAL_PRICE = (By.CSS_SELECTOR, "span[class*='styles__CartSummarySpan-sc-odscpb-3']")

    def verify_cart_empty_message(self):
       self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart_items(self, amount):
        cart_summary_text = self.find_element(*self.CART_SUMMARY).text
        assert amount in cart_summary_text, f"Expected {amount} items but got {cart_summary_text}"

    def verify_product_name(self, item):
        actual_name = self.find_element(*self.CART_ITEM_TITLE).text
        assert item in actual_name, f"Expected {item} but got {actual_name}"

