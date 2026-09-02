import allure
from api.courier_api import CourierAPI
from helpers.data_generator import generate_random_string
from config import ERROR_MESSAGES

@allure.feature('Логин курьера')
class TestCourierLogin:
    
    @allure.title('Курьер может авторизоваться')
    def test_login_courier_success(self, create_and_delete_courier):
        courier = create_and_delete_courier
        assert courier is not None
        response = CourierAPI.login_courier(courier['login'], courier['password'])
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title('Для авторизации нужно передать все обязательные поля')
    def test_login_required_fields(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        
        response1 = CourierAPI.login_courier(login, '')
        assert response1.status_code == 400
        assert ERROR_MESSAGES["missing_login_data"] in response1.json()["message"]
        
        response2 = CourierAPI.login_courier('', password)
        assert response2.status_code == 400
        assert ERROR_MESSAGES["missing_login_data"] in response2.json()["message"]

    @allure.title('Система вернёт ошибку при неверном логине или пароле')
    def test_login_wrong_credentials(self, create_and_delete_courier):
        courier = create_and_delete_courier
        assert courier is not None
        
        response1 = CourierAPI.login_courier('wrong_login', courier['password'])
        assert response1.status_code == 404
        assert response1.json()["message"] == ERROR_MESSAGES["courier_not_found"]
        
        response2 = CourierAPI.login_courier(courier['login'], 'wrong_password')
        assert response2.status_code == 404
        assert response2.json()["message"] == ERROR_MESSAGES["courier_not_found"]

    @allure.title('Если авторизоваться под несуществующим пользователем, возвращается ошибка')
    def test_login_nonexistent_user(self):
        fake_login = generate_random_string(10)
        fake_password = generate_random_string(10)
        response = CourierAPI.login_courier(fake_login, fake_password)
        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES["courier_not_found"]