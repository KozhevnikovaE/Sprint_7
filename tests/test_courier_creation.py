import pytest
import allure
from api.courier_api import CourierAPI
from helpers.data_generator import generate_random_string
from config import ERROR_MESSAGES

@allure.feature('Создание курьера')
class TestCourierCreation:
    
    @allure.title('Курьера можно создать')
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        response = CourierAPI.create_courier(login, password, first_name)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        
        response1 = CourierAPI.create_courier(login, password, first_name)
        assert response1.status_code == 201
        
        response2 = CourierAPI.create_courier(login, password, first_name)
        assert response2.status_code == 409
        assert response2.json()["message"] == ERROR_MESSAGES["duplicate_login"]

    @allure.title('Для создания курьера нужно передать все обязательные поля')
    @pytest.mark.parametrize('login, password', [
        ('', generate_random_string(10)),  # Без логина
        (generate_random_string(10), ''),   # Без пароля
    ])
    def test_create_courier_missing_fields(self, login, password):
        response = CourierAPI.create_courier(login, password)
        assert response.status_code == 400
        assert ERROR_MESSAGES["missing_fields"] in response.json()["message"]