import allure
import requests


class CompanyApi:
    """
        Класс для взаимодействия с API компании.

        Attributes:
            url (str): URL API компании.
    """

    def __init__(self, url):
        """
            Инициализация объекта CompanyApi.

            Args:
                url (str): URL API компании.
        """
        self.url = url

    @allure.step("api. Получить список фильтров по квартирам")
    def get_filters_list(self, params_to_add=None):
        """
            Получить список фильтров по квартирам.

                Args:
                    params_to_add (dict, optional): Дополнительные параметры запроса.

                Returns:
                    dict: Список фильтров в формате JSON.
        """
        resp = requests.get(self.url + '/realty/flat/facts', params=params_to_add)
        return resp.json()

    @allure.step("api. Получить список всех квартир")
    def get_flats_list(self, params_to_add=None):
        """
            Получить список всех квартир.

            Args:
                params_to_add (dict, optional): Дополнительные параметры запроса.

            Returns:
                dict: Список квартир в формате JSON.
        """
        resp = requests.get(self.url + '/realty/flat', params=params_to_add)
        return resp.json()

    @allure.step("api. Получить информацию о конкретной квартире")
    def get_info_flat_list(self, params_to_add=None):
        """
            Получить информацию о конкретной квартире.

                Args:
                    params_to_add (dict, optional): Дополнительные параметры запроса.

                Returns:
                    dict: Информация о квартире в формате JSON.
        """
        resp = requests.get(self.url + '/realty/flat/6009669', params=params_to_add)
        return resp.json()

    @allure.step("api. Получить контакты для связи с компанией")
    def get_contact_list(self, params_to_add=None):
        """
            Получить контакты для связи с компанией.

            Args:
                params_to_add (dict, optional): Дополнительные параметры запроса.

            Returns:
                dict: Контактная информация в формате JSON.
        """
        resp = requests.get(self.url + '/contact', params=params_to_add)
        return resp.json()

    @allure.step("api. Получить информацию по ставке по умолчанию")
    def get_stavka_list(self, params_to_add=None):
        """
            Получить информацию по ставке по умолчанию.

            Args:
                params_to_add (dict, optional): Дополнительные параметры запроса.

            Returns:
                dict: Информация о ставке в формате JSON.
        """
        resp = requests.get(self.url + '/stavka-po-umolchaniyu', params=params_to_add)
        return resp.json()
