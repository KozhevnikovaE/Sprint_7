import allure
import requests
from config import BASE_URL

class CourierAPI:
    @staticmethod
    @allure.step("Создание курьера с логином: {login}")
    def create_courier(login, password, first_name=None):
        payload = {"login": login, "password": password}
        if first_name:
            payload["firstName"] = first_name
        return requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

    @staticmethod
    @allure.step("Логин курьера с логином: {login}")
    def login_courier(login, password):
        payload = {"login": login, "password": password}
        return requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

    @staticmethod
    @allure.step("Удаление курьера с id: {courier_id}")
    def delete_courier(courier_id):
        return requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')