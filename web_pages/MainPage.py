from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """
        Класс с методами для главной страницы.

        Attributes:
            driver (WebDriver): Экземпляр WebDriver для управления браузером.
    """

    def __init__(self, driver: WebDriver):
        """
            Инициализация MainPage.

            :param driver: Экземпляр WebDriver для управления браузером.
        """
        self._driver: WebDriver = driver
        self._driver.get("https://kronverk.bureausuchkov.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    @allure.step("Клик по избранным квартирам")
    def favorite_apartments(self):
        """
            Клик по избранным квартирам (на выходе ожидаем страницу с текстом "ИЗБРАННОЕ").
        """
        WebDriverWait(self._driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/favorites"]'))
        ).click()

    @allure.step("Клик по квартирам")
    def all_apartments(self):
        """
            Клик по квартирам (на выходе ожидаем страницу с текстом "ПОДОБРАТЬ КВАРТИРУ").
        """
        WebDriverWait(self._driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/apartments"]'))
        ).click()

    @allure.step("Клик на способы покупки")
    def how_to_buy(self):
        """
            Клик на способы покупки (на выходе ожидаем страницу с текстом "СПОСОБЫ ПОКУПКИ").
        """
        WebDriverWait(self._driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/how-to-buy"]'))
        ).click()

    @allure.step("Клик на 'Связаться с нами'")
    def contact_with_us(self):
        """
            Клик на "Связаться с нами" (на выходе ожидаем страницу с текстом "ПОЛУЧИТЬ КОНСУЛЬТАЦИЮ").

            Обрабатывает исключение TimeoutException, если кнопка не найдена или не кликабельна.
        """
        try:
            button = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="__nuxt"]/header/div/div/div[3]/div/div[1]/button'))
            )
            button.click()
        except TimeoutException:
            print("Button with text 'Связаться с нами' not found or not clickable")
            self._driver.quit()
            raise

    @allure.step("Клик на бургер-меню")
    def burger_menu(self):
        """
            Клик на Бургер-меню (на выходе ожидаем список).
        """
        menu_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header button'))
        )
        menu_button.click()
