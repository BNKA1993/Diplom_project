from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class ResultPages:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def favorite_apartments_is_open(self):
        WebDriverWait(self._driver, 30).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"), "ИЗБРАННОЕ")
        )
        txt = self._driver.find_element(By.CSS_SELECTOR, "h1").text
        return txt

    def all_apartments_is_open(self):
        WebDriverWait(self._driver, 30).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"), "ПОДОБРАТЬ")
        )
        txt = self._driver.find_element(By.CSS_SELECTOR, "h1").text
        return txt

    def how_to_buy_is_open(self):
        WebDriverWait(self._driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        h1_element = self._driver.find_element(By.CSS_SELECTOR, "h1")
        # Получаем весь текст из элемента h1, включая текст из всех его дочерних элементов
        txt = h1_element.get_property('innerText')
        return txt

    def contact_with_us_is_open(self):
        WebDriverWait(self._driver, 50).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="consultation"]/div[2]/div/section/div[1]/div/div[2]/div/div/h1'))
        )
        h1_element = self._driver.find_element(By.XPATH,
                                               '//*[@id="consultation"]/div[2]/div/section/div[1]/div/div[2]/div/div/h1')
        txt = h1_element.get_property('innerText')
        return txt

    def burger_menu_is_open(self):
        # Ожидание появления элементов меню и получение их текстов
        menu_items = WebDriverWait(self._driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav a'))
        )
        WebDriverWait(self._driver, 30).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'nav a'))
        )
        # Получение текста для всех элементов меню с проверкой их видимости
        actual_menu_titles = []
        for item in menu_items:
            WebDriverWait(self._driver, 10).until(
                EC.visibility_of(item)
            )
            actual_menu_titles.append(item.text)
        return actual_menu_titles
