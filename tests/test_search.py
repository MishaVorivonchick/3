import time

from page.form_pages import HomePage
from conftest import driver


class TestFormPage:
    def test_form (self, driver):
        form_page = HomePage(driver)
        form_page.open()
        form_page.search_and_sumbit()
