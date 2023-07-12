import time

import allure
from selenium.webdriver import Keys

from page.base_page import BasePage
from locators.home_page_locators import HomePageLocators as Locators


class HomePage(BasePage):

    def search_and_sumbit(self):
        text = "Пылесосы"
        self.find_element(Locators.CATALOG_SEARCH).send_keys(text)
        time.sleep(3)
        self.find_element(Locators.CATALOG_SEARCH).send_keys(Keys.ENTER)
        time.sleep(3)

