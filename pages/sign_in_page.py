from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    # T_C_Link = (By.CSS_SELECTOR, "a[href='/c/target-privacy-policy/-/N-4sr7p'].styles__StyledLink-sc-vpsldm-0")
    T_C_LINK = (By.CSS_SELECTOR, "a[href='/c/terms-conditions/-/N-4sr7l'].styles__StyledLink-sc-vpsldm-0")

    def open_sign_in_page(self):
        self.open_url('https://www.target.com/login')

    def click_t_c_link(self):
        self.wait_until_clickable(*self.T_C_LINK)
