from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
from pages.ResultPage import ResultPages

expected_menu_titles = [
    "ПРОЕКТЫ", "КВАРТИРЫ", "СПОСОБЫ ПОКУПКИ", "О КОМПАНИИ",
    "МЕДИА", "КОММЕРЧЕСКАЯ", "КОНТАКТЫ", "ДОКУМЕНТЫ"
]


def test_favorite_apartments():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.favorite_apartments()

    result_page = ResultPages(browser)
    to_be = result_page.favorite_apartments_is_open()
    as_is = "ИЗБРАННОЕ"

    assert as_is in to_be, f"Expected text to contain '{as_is}' but got '{to_be}'"
    browser.quit()


def test_all_apartments():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.all_apartments()

    result_page = ResultPages(browser)
    to_be = result_page.all_apartments_is_open()
    to_be_words = ["ПОДОБРАТЬ", "КВАРТИРУ"]

    for word in to_be_words:
        assert word in to_be, f"Expected word '{word}' not found in '{to_be}'"

    browser.quit()


def test_contact_with_us():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.contact_with_us()

    result_page = ResultPages(browser)
    to_be = result_page.contact_with_us_is_open()
    to_be_words = ["ЗАКАЗАТЬ", "КОНСУЛЬТАЦИЮ"]

    assert any(word in to_be for word in to_be_words), f"Expected text '{to_be_words}' not found in '{to_be}'"

    browser.quit()


def test_how_to_buy():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.how_to_buy()

    result_page = ResultPages(browser)
    to_be = result_page.how_to_buy_is_open()
    to_be_words = ["СПОСОБЫ", "ПОКУПКИ"]

    for word in to_be_words:
        assert word in to_be, f"Expected word '{word}' not found in '{to_be}'"

    browser.quit()


def test_result_burger_menu():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.burger_menu()

    result_page = ResultPages(browser)
    to_be = result_page.burger_menu_is_open()

    as_is = expected_menu_titles
    # Проверка названий пунктов меню
    assert to_be == as_is

    browser.quit()
