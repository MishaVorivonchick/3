import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import home_page_locators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def open(self):
        with allure.step("Перейти на главную страницу"):
            self.driver.get('https://www.onliner.by/')

    def find_element(self, *args):
        """ Метод find_element() принимает два аргумента:
            by_name и by_val, которые определяют, как искать
            элемент на странице. Метод использует self.driver
            для поиска элемента на странице и возвращает найденный элемент"""

        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def is_element_visible(self, *args):
        """ Метод is_element_visible() также принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент на странице.
            Метод использует WebDriverWait для ожидания видимости
            элемента на странице в течение 10 секунд, после чего
            он возвращает найденный элемент. Если элемент не появляется
            на странице в течение 10 секунд, возникает исключение TimeoutException"""

        by_name, by_val = args[0]
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by_name, by_val))
        )
        return self.driver.find_element(by_name, by_val)

    def is_not_element_present(self, *args):
        """ Метод is_not_element_present() проверяет, что элемент не появляется
            на странице в течение 10 секунд. Метод принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент на странице.
            Метод использует WebDriverWait для ожидания отсутствия элемента на
            странице в течение 10 секунд. Если элемент не появляется на
            странице в течение 10 секунд, метод возвращает True. Если элемент
            все же появляется, возникает исключение TimeoutException, и метод возвращает False"""

        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def is_element_present(self, *args):
        """ Метод is_element_present() проверяет, что элемент появляется
            на странице в течение 10 секунд. Метод принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент
            на странице. Метод использует WebDriverWait для ожидания
            появления элемента на странице в течение 10 секунд. Если элемент
            появляется на странице в течение 10 секунд, метод возвращает True.
            Если элемент не появляется, возникает исключение TimeoutException,
            и метод возвращает False"""

        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def find_elements(self, *args):
        """ Метод find_elements() находит все элементы на странице,
            соответствующие заданным параметрам поиска. Метод принимает
            два аргумента: by_name и by_val, которые определяют,
            как искать элементы на странице. Метод использует self.driver
            для поиска элементов на странице и возвращает найденные элементы"""

        by_name, by_val = args[0]
        return self.driver.find_elements(by_name, by_val)

    def go_to_main_page(self):
        """ Метод go_to_main_page() переходит на главную страницу.
            Метод использует метод is_element_visible() для поиска
            элемента с логотипом на странице и кликает на него.
            Метод is_element_visible() ожидает, что элемент с
            логотипом появится на странице и станет видимым в течение 10 секунд.
            Если элемент не появляется на странице в течение 10 секунд,
            возникает исключение TimeoutException"""

        self.is_element_visible(home_page_locators.header_logo).click()

    def get_current_url(self):
        """ Метод get_current_url() возвращает текущий URL-адрес страницы"""

        return self.driver.current_url

    def is_elements_text_equal_to(self, *args, element_text):
        """ Метод is_elements_text_equal_to() проверяет,
            что текст элемента соответствует заданному значению.
            Метод принимает два аргумента: by_name и by_val,
            которые определяют, как искать элемент на странице,
            и element_text - текст, который должен быть найден в элементе.
            Метод использует WebDriverWait для ожидания
            появления элемента на странице в течение 10 секунд.
            Если текст элемента соответствует заданному значению,
            метод возвращает True. Если текст элемента не соответствует
            заданному значению, возникает исключение TimeoutException,
            и метод возвращает False"""

        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((by_name, by_val), element_text),
            )
        except TimeoutException:
            return False
        return True

    def drag_and_drop_from_right_to_left(self, source, x_offset=0, y_offset=0):
        """ Метод drag_and_drop_from_right_to_left() выполняет перетаскивание
            элемента справа налево. Метод принимает два аргумента: source - элемент,
            который нужно перетащить, и x_offset, y_offset - смещение на которое
            нужно перетащить элемент. Метод использует метод find_element() для
            поиска элемента на странице, создает объект ActionChains, который
            используется для выполнения перетаскивания элемента. x_offset и y_offset
            используются для указания смещения, на которое нужно перетащить элемент.
            Если не указано смещение, элемент будет перетаскиваться на ту же позицию,
            где он находится на странице"""

        source_web_element = self.find_element(source)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source_web_element, x_offset, y_offset).perform()

    def check_for_url_is_changed(self, current_url, url_that_should_be):
        """ Метод check_for_url_is_changed() проверяет,
            что URL-адрес страницы изменился. Метод принимает два аргумента: current_url
            - текущий URL-адрес страницы и url_that_should_be - URL-адрес,
            который должен быть после выполнения действия. Метод сравнивает
            текущий URL-адрес страницы с ожидаемым URL-адресом. Если текущий
            URL-адрес отличается от ожидаемого, возникает исключение AssertionError.
            Если URL-адрес соответствует ожидаемому, метод ничего не возвращает"""

        with allure.step(f"Проверяем, что текущий url равен {url_that_should_be}"):
            assert current_url == url_that_should_be