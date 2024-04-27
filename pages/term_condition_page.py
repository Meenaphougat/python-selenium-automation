from pages.base_page import Page


class TermConditionPage(Page):
    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/')

