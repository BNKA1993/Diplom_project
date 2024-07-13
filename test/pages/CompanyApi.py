import requests


class CompanyApi:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    # получить список фильтров по квартирам
    def get_filters_list(self, params_to_add=None):
        resp = requests.get(self.url + '/realty/flat/facts', params=params_to_add)
        return resp.json()

    # получить список фильтров по квартирам
    def get_flats_list(self, params_to_add=None):
        resp = requests.get(self.url + '/realty/flat', params=params_to_add)
        return resp.json()

    # создание заявки
    def create_ticket(self, data):
        resp = requests.post(self.url + '/tickets', json=data)
        return resp
