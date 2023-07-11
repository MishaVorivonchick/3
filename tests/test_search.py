from page.form_pages import FormPage


class TestFormPage:
    def test_form (self, driver):
        form_page = FormPage(driver,"https://www.onliner.by/")
        form_page.open()
        form_page.search_and_sumbit()