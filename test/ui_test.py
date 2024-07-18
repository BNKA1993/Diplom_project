import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from web_pages.MainPage import MainPage
from web_pages.ResultPage import ResultPages

expected_menu_titles = [
    "ПРОЕКТЫ", "КВАРТИРЫ", "СПОСОБЫ ПОКУПКИ", "О КОМПАНИИ",
    "МЕДИА", "КОММЕРЧЕСКАЯ", "КОНТАКТЫ", "ДОКУМЕНТЫ"
]


@allure.severity("critical")
@allure.id("Kronverk-UI-1")
@allure.story("Переход на страницу с квартирами, добавленными в избранное")
@allure.title("Открытие страницы Избранное")
@pytest.mark.ui_test
def test_favorite_apartments():
    with allure.step("Инициализация браузера и открытие главной страницы"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        main_page = MainPage(browser)
    with allure.step("Переход на страницу Избранное"):
        main_page.favorite_apartments()

    with allure.step("Проверка открытия страницы Избранное"):
        result_page = ResultPages(browser)
        to_be = result_page.favorite_apartments_is_open()
        as_is = "ИЗБРАННОЕ"
        assert as_is in to_be, f"Expected text to contain '{as_is}' but got '{to_be}'"

    with allure.step("Закрытие браузера"):
        browser.quit()


@allure.severity("critical")
@allure.id("Kronverk-UI-2")
@allure.story("Переход на страницу со всеми квартирами")
@allure.title("Открытие страницы квартир")
@pytest.mark.ui_test
def test_all_apartments():
    with allure.step("Инициализация браузера и открытие главной страницы"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        main_page = MainPage(browser)
    with allure.step("Переход на страницу со всеми квартирами"):
        main_page.all_apartments()

    with allure.step("Проверка открытия страницы всех квартир"):
        result_page = ResultPages(browser)
        to_be = result_page.all_apartments_is_open()
        to_be_words = ["ПОДОБРАТЬ", "КВАРТИРУ"]

        for word in to_be_words:
            assert word in to_be, f"Expected word '{word}' not found in '{to_be}'"

    with allure.step("Закрытие браузера"):
        browser.quit()


@allure.severity("critical")
@allure.id("Kronverk-UI-3")
@allure.story("Переход на страницу получения консультации")
@allure.title("Открытие страницы с формой для заполнения")
@pytest.mark.ui_test
def test_contact_with_us():
    with allure.step("Инициализация браузера и открытие главной страницы"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        main_page = MainPage(browser)
    with allure.step("Переход на страницу Контакты"):
        main_page.contact_with_us()

    with allure.step("Проверка открытия страницы Контакты"):
        result_page = ResultPages(browser)
        to_be = result_page.contact_with_us_is_open()
        to_be_words = ["ЗАКАЗАТЬ", "КОНСУЛЬТАЦИЮ"]
        assert any(word in to_be for word in to_be_words), f"Expected text '{to_be_words}' not found in '{to_be}'"

    with allure.step("Закрытие браузера"):
        browser.quit()


@allure.severity("critical")
@allure.id("Kronverk-UI-4")
@allure.story("Переход на страницу со способами покупки")
@allure.title("Открытие страницы способов покупки")
@pytest.mark.ui_test
def test_how_to_buy():
    with allure.step("Инициализация браузера и открытие главной страницы"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        main_page = MainPage(browser)
    with allure.step("Переход на страницу способов покупки"):
        main_page.how_to_buy()

    with allure.step("Проверка открытия страницы способов покупки"):
        result_page = ResultPages(browser)
        to_be = result_page.how_to_buy_is_open()
        to_be_words = ["СПОСОБЫ", "ПОКУПКИ"]

        for word in to_be_words:
            assert word in to_be, f"Expected word '{word}' not found in '{to_be}'"

    with allure.step("Закрытие браузера"):
        browser.quit()


@allure.severity("critical")
@allure.id("Kronverk-UI-5")
@allure.story("Разворачивание содержимого бургер-меню")
@allure.title("Открытие бургер-меню")
@pytest.mark.ui_test
def test_result_burger_menu():
    with allure.step("Инициализация браузера и открытие главной страницы"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        main_page = MainPage(browser)
    with allure.step("Открытие бургер-меню"):
        main_page.burger_menu()

    with allure.step("Проверка содержимого бургер-меню"):
        result_page = ResultPages(browser)
        to_be = result_page.burger_menu_is_open()

        as_is = expected_menu_titles
        assert to_be == as_is

    with allure.step("Закрытие браузера"):
        browser.quit()
