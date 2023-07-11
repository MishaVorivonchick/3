from selenium.webdriver.common.by import By
class FormPageLocators:
    CATALOG_SEARCH = (By.XPATH, "//*[@id='fast-search']/form/input[1]")
    CATALOG_BUTTON = (By.XPATH, "//*[@id='container']/div/div/header/div[2]/div/nav/ul[1]/li[1]/a[2]/span")
    EMAIL = (By.XPATH, "//div[@class='auth-form__row auth-form__row_condensed-alter']//input")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, '//*[@id="auth-container"]/div/div[2]/div/form/div[3]')
    CURRENCY_BUYING = (By.XPATH, "//span[@class= '_u js-currency-amount']")
    SECTION_ELECTRONICS = (By.XPATH, "//li[@data-id = 1]")
    USD_SALE = (By.XPATH, "//table[@class='b-currency-table__best'][1]//td[3]//b")
    USD_BUYING = (By.XPATH, "//table[@class='b-currency-table__best'][1]//td[2]//b")