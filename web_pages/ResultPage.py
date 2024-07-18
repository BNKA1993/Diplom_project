from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class ResultPages:
    """
        Класс с методами для проверки открытия различных страниц.

        Attributes:
            "driver" (WebDriver): Экземпляр WebDriver для управления браузером.
    """

    def __init__(self, driver: WebDriver):
        """
            Инициализация ResultPages.

            :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver = driver

    @allure.step("Проверка открытия страницы 'ИЗБРАННОЕ'")
    def favorite_apartments_is_open(self):
        """
            Проверяет, открыта ли страница с текстом "ИЗБРАННОЕ".

            Ожидает, пока текст "ИЗБРАННОЕ" не появится в элементе с CSS селектором "h1".

            :return: Текст элемента "h1".
        """
        WebDriverWait(self._driver, 30).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"), "ИЗБРАННОЕ")
        )
        txt = self._driver.find_element(By.CSS_SELECTOR, "h1").text
        return txt

    @allure.step("Проверка открытия страницы 'ПОДОБРАТЬ'")
    def all_apartments_is_open(self):
        """
            Проверяет, открыта ли страница с текстом "ПОДОБРАТЬ".

            Ожидает, пока текст "ПОДОБРАТЬ" не появится в элементе с CSS селектором "h1".

            :return: Текст элемента "h1".
        """
        WebDriverWait(self._driver, 30).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"), "ПОДОБРАТЬ")
        )
        txt = self._driver.find_element(By.CSS_SELECTOR, "h1").text
        return txt

    @allure.step("Проверка открытия страницы 'СПОСОБЫ ПОКУПКИ'")
    def how_to_buy_is_open(self):
        """
            Проверяет, открыта ли страница "СПОСОБЫ ПОКУПКИ".

            Ожидает, пока элемент с CSS селектором "h1" не станет присутствовать на странице.

            :return: Весь текст элемента "h1", включая текст из всех его дочерних элементов.
        """
        WebDriverWait(self._driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        h1_element = self._driver.find_element(By.CSS_SELECTOR, "h1")
        txt = h1_element.get_property('innerText')
        return txt

    @allure.step("Проверка открытия страницы 'ПОЛУЧИТЬ КОНСУЛЬТАЦИЮ'")
    def contact_with_us_is_open(self):
        """
            Проверяет, открыта ли страница "ПОЛУЧИТЬ КОНСУЛЬТАЦИЮ".

            Ожидает, пока элемент с XPath не станет присутствовать на странице.

            :return: Весь текст элемента "h1", включая текст из всех его дочерних элементов.
        """
        WebDriverWait(self._driver, 50).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="consultation"]/div[2]/div/section/div[1]/div/div[2]/div/div/h1'))
        )
        h1_element = self._driver.find_element(By.XPATH,
                                               '//*[@id="consultation"]/div[2]/div/section/div[1]/div/div[2]/div/div/h1')
        txt = h1_element.get_property('innerText')
        return txt

    @allure.step("Проверка открытия бургер-меню")
    def burger_menu_is_open(self):
        """
            Проверяет, открыто ли бургер-меню.

            Ожидает появления и видимости всех элементов меню с CSS селектором 'nav a'.
            Собирает текст для всех элементов меню.

            :return: Список текстов элементов меню.
        """
        menu_items = WebDriverWait(self._driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav a'))
        )
        WebDriverWait(self._driver, 30).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'nav a'))
        )
        actual_menu_titles = []
        for item in menu_items:
            WebDriverWait(self._driver, 10).until(
                EC.visibility_of(item)
            )
            actual_menu_titles.append(item.text)
        return actual_menu_titles
