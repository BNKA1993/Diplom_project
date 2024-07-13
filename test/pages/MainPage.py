from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# класс с методами для главной страницы
class MainPage:
    def __init__(self, driver: WebDriver):
        self._driver: WebDriver = driver
        self._driver.get("https://kronverk.bureausuchkov.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    # клик по избранному (на выходе ожидаем страницу с текстом "ИЗБРАННОЕ")
    def favorite_apartments(self):
        WebDriverWait(self._driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/favorites"]'))
        ).click()

    # Клик по квартирам(на выходе ожидаем страницу с текстом "ПОДОБРАТЬ КВАРТИРУ")
    def all_apartments(self):
        WebDriverWait(self._driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/apartments"]'))
        ).click()

    # Клик на способы покупки(на выходе ожидаем страницу с текстом "СПОСОБЫ ПОКУПКИ"
    def how_to_buy(self):
        WebDriverWait(self._driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/how-to-buy"]'))
        ).click()

    # Клик на "Связаться с нами" (На выходе ожидаем страницу с текстом "ПОЛУЧИТЬ КОНСУЛЬТАЦИЮ"
    def contact_with_us(self):
        try:
            button = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="__nuxt"]/header/div/div/div[3]/div/div[1]/button'))
            )
            button.click()
        except TimeoutException:
            print("Button with text 'Связаться с нами' not found or not clickable")
            self._driver.quit()
            raise

    # Клик на Бургер-меню(на выходе ожидаем список)
    def burger_menu(self):
        menu_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'header button'))
        )
        menu_button.click()
