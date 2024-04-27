from selenium.webdriver.common.by import By
from pages.base_page import Page


class TargetAppPage(Page):
    PP_link = (By.XPATH, "//a[text()='Privacy policy']")

    def open_target_app(self):
        self.open_url('https://www.target.com/c/target-app/')

    def click_pp_link(self):
        self.wait_until_clickable(*self.PP_link)

