import allure
from api.courier_api import CourierAPI
from helpers.data_generator import generate_random_string
from config import ERROR_MESSAGES

@allure.feature('Логин курьера')
class TestCourierLogin:
    
    @allure.title('Курьер может авторизоваться')
    def test_login_courier_success(self, create_and_delete_courier):
        courier = create_and_delete_courier
        
        response = CourierAPI.login_courier(courier['login'], courier['password'])
        assert response.status_code == 200
        assert "id" in response.json()


    @allure.title('Авторизация: ошибка при отсутствии логина')
    def test_login_without_login(self):
        login = ''
        password = generate_random_string(10)

        response = CourierAPI.login_courier(login, password)
        assert response.status_code == 400
        assert ERROR_MESSAGES["missing_login_data"] in response.json()["message"]


    @allure.title('Авторизация: ошибка при отсутствии пароля')
    def test_login_without_password(self):
        login = generate_random_string(10)
        password = ''

        response = CourierAPI.login_courier(login, password)
        assert response.status_code == 400
        assert ERROR_MESSAGES["missing_login_data"] in response.json()["message"]

    @allure.title('Система вернёт ошибку, если указан неверный логин курьера')
    def test_login_wrong_login(self, create_and_delete_courier):
        courier = create_and_delete_courier
        
        response = CourierAPI.login_courier('wrong_login', courier['password'])
    
        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES["courier_not_found"]


    @allure.title('Система вернёт ошибку, если указан неверный пароль курьера')
    def test_login_wrong_password(self, create_and_delete_courier):
        courier = create_and_delete_courier
  
        response = CourierAPI.login_courier(courier['login'], 'wrong_password')
    
        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES["courier_not_found"]

    @allure.title('Если авторизоваться под несуществующим пользователем, возвращается ошибка')
    def test_login_nonexistent_user(self):
        fake_login = generate_random_string(10)
        fake_password = generate_random_string(10)
        response = CourierAPI.login_courier(fake_login, fake_password)
        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES["courier_not_found"]