import requests
import pytest

from pages.CompanyApi import CompanyApi

api = CompanyApi("https://api-kronverk.bureausuchkov.com/api")


# Проверка получения списка фильтров
def test_get_filters():
    body = api.get_filters_list()
    assert len(body) > 0


# Проверка получения списка фильтров
def test_get_flats():
    body = api.get_flats_list()
    assert len(body) > 0


# Параметризация данных для теста создания заявки с позитивным именем
@pytest.mark.parametrize("ticket_data", [
    {
        "data": {
            "name": "Виктория",
            "phone": "+7 (999) 999-99-99",
            "message": "Страница: /company, Тип: Звонок | Время: Сегодня  Консультация",
            "action": "callback",
            "channel_medium": "callback",
            "utm": {}
        }
    },
    {
        "data": {
            "name": "Dmitrii",
            "phone": "+7 (999) 999-99-99",
            "message": "Страница: /service, Тип: Чат | Время: Завтра  Консультация",
            "action": "chat",
            "channel_medium": "chat",
            "utm": {}
        }
    },
    {
        "data": {
            "name": "марина",
            "phone": "+7 (999) 999-99-99",
            "message": "Страница: /company, Тип: Звонок | Время: Сегодня  Консультация",
            "action": "callback",
            "channel_medium": "callback",
            "utm": {}
        }
    },
    {
        "data": {
            "name": "АННА",
            "phone": "+7 (999) 999-99-99",
            "message": "Страница: /company, Тип: Звонок | Время: Сегодня  Консультация",
            "action": "callback",
            "channel_medium": "callback",
            "utm": {}
        }
    },
    {
        "data": {
            "name": "София Романова",
            "phone": "+7 (999) 999-99-99",
            "message": "Страница: /company, Тип: Звонок | Время: Сегодня  Консультация",
            "action": "callback",
            "channel_medium": "callback",
            "utm": {}
        }
    },
    {
        "data": {
            "name": "ИмяИмяИмяИмяИмяИмяИмяИмяИмяИмяИмяИмяИмяИмяИмяИмяИ",
            "phone": "+7 (999) 999-99-99",
            "message": "Страница: /company, Тип: Звонок | Время: Сегодня  Консультация",
            "action": "callback",
            "channel_medium": "callback",
            "utm": {}
        }
    },
    {
        "data": {
            "name": "А",
            "phone": "+7 (999) 999-99-99",
            "message": "Страница: /company, Тип: Звонок | Время: Сегодня  Консультация",
            "action": "callback",
            "channel_medium": "callback",
            "utm": {}
        }
    }
])
def test_create_ticket_with_positive_name(ticket_data):
    response = api.create_ticket(ticket_data)
    assert response.status_code == 200
    response_data = response.json()
    assert 'id' in response_data['data']


# Тест для проверки создания заявки с позитивным телефоном
def test_create_ticket():
    ticket_data = {
        "data": {
            "name": "Виктория",
            "phone": "+7 (123) 456-78-90",
            "message": "Страница: /company, Тип: Звонок | Время: Сегодня Консультация",
            "action": "callback",
            "channel_medium": "callback",
            "utm": {}
        }
    }
    response = api.create_ticket(ticket_data)
    response_json = response.json()
    assert 'id' in response_json
