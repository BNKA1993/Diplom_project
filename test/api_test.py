import pytest
import allure

from web_pages.CompanyApi import CompanyApi

api = CompanyApi("https://api-kronverk.bureausuchkov.com/api")


@allure.severity("normal")
@allure.id("Kronverk-API-1")
@allure.story("Получение списка всех фильтров")
@allure.title("Получение списка всех фильтров")
@pytest.mark.api_test
def test_get_filters():
    with allure.step("Получение списка фильтров через API"):
        body = api.get_filters_list()
    with allure.step("Проверка, что список фильтров не пустой"):
        assert len(body) > 0


@allure.id("Kronverk-API-2")
@allure.story("Получение списка всех квартир")
@allure.title("Получение списка всех квартир")
@pytest.mark.api_test
def test_get_flats():
    with allure.step("Получение списка квартир через API"):
        body = api.get_flats_list()
    with allure.step("Проверка, что список фильтров не пустой"):
        assert len(body) > 0


@allure.id("Kronverk-API-3")
@allure.story("Получение информации о квартире")
@allure.title("Получение информации о квартире")
@pytest.mark.api_test
def test_get_info_about_flat():
    with allure.step("Получение информации о квартире через API"):
        response = api.get_info_flat_list()
    with allure.step("Извлечение данных о квартире"):
        data = response['data']
    with allure.step("Проверка ID квартиры"):
        flat_id = data['id']
        required_id = 6009669
        assert flat_id == required_id, f"ID в ответе {flat_id} не соответствует ожидаемому ID {required_id}"


@allure.id("Kronverk-API-4")
@allure.story("Получение списка контактов для связи")
@allure.title("Получение списка контактов для связи")
@pytest.mark.api_test
def test_get_contact():
    with allure.step("Получение списка контактов через API"):
        body = api.get_contact_list()
    with allure.step("Проверка, что список контактов не пустой"):
        assert len(body) > 0


@allure.id("Kronverk-API-5")
@allure.story("Получение списка ставок по умолчанию")
@allure.title("Получение списка ставок")
@pytest.mark.api_test
def test_get_stavka():
    with allure.step("Получение списка ставок через API"):
        body = api.get_stavka_list()
    with allure.step("Проверка, что список ставок не пуст"):
        assert len(body) > 0
