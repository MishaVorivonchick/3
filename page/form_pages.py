import time

from page.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):
    def search_and_sumbit(self):
        text = "пылесос"
        self.element_are_visible(Locators.CATALOG_SEARCH).send_keys(text)
        self.element_are_visible(Locators.CATALOG_BUTTON).click
        time.sleep(5)
        return text
