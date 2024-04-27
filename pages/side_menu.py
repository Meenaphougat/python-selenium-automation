from selenium.webdriver.common.by import By
from pages.base_page import Page


class SideMenu(Page):
    SIGN_IN_BTN_SIDE_NAV = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def click_inside(self):
        self.wait_until_clickable(*self.SIGN_IN_BTN_SIDE_NAV)
