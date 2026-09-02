import allure
import requests
from helpers.data_generator import generate_random_string
from config import BASE_URL

class ApiHelpers:
    @staticmethod
    @allure.step("Регистрация нового курьера")
    def register_new_courier_and_return_login_password():
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)
        
        if response.status_code == 201:
            return [login, password, first_name]
        return []