import allure
import requests
from helpers.data_generator import generate_random_string
from config import BASE_URL

class ApiHelpers:
    @staticmethod
    @allure.step("Регистрация нового курьера")
    def register_new_courier():
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

        # ВАЖНО: сначала получаем JSON-тело ответа в переменную body
        if response.status_code == 201:
            body = response.json()  # <--- ЭТА СТРОКА БЫЛА ПРОПУЩЕНА
            return {
                "login": login,
                "password": password,
                "first_name": first_name,
                "id": body.get("id"),
            }

        raise RuntimeError(
            f"Не удалось создать курьера. Статус: {response.status_code}, "
            f"ответ: {response.text}"
        )

    