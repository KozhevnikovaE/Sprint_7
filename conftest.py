import pytest
from api.api_helpers import ApiHelpers
from helpers.data_generator import get_order_data, generate_random_string
from api.courier_api import CourierAPI

@pytest.fixture
def create_and_delete_courier():
    """Фикстура: создаёт курьера и удаляет после теста"""
    courier_data = ApiHelpers.register_new_courier_and_return_login_password()
    if courier_data:
        login, password, first_name = courier_data
        yield {"login": login, "password": password, "first_name": first_name}
        response = CourierAPI.login_courier(login, password)
        if response.status_code == 200:
            courier_id = response.json().get("id")
            if courier_id:
                CourierAPI.delete_courier(courier_id)
    else:
        yield None

@pytest.fixture
def generate_order_data():
    """Фикстура, которая возвращает данные для заказа из data_generator.py"""
    return get_order_data()

@pytest.fixture
def courier_cleanup():
    """Не создаёт курьера. Тест сам создаёт, а фикстура удаляет после."""
    credentials = {}
    yield credentials
    if credentials:
        response = CourierAPI.login_courier(credentials['login'], credentials['password'])
        if response.status_code == 200 and 'id' in response.json():
            courier_id = response.json()['id']
            CourierAPI.delete_courier(courier_id)


@pytest.fixture
def existing_courier():
    """Создаёт курьера и возвращает его данные; удаляет после теста."""
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    response = CourierAPI.create_courier(login, password, first_name)
    assert response.status_code == 201, "Не удалось создать курьера для фикстуры"

    courier_data = {
        "login": login,
        "password": password,
        "first_name": first_name,
    }

    yield courier_data
    courier_id = response.json().get("id")
    if courier_id:
        delete_response = CourierAPI.delete_courier(courier_id)


