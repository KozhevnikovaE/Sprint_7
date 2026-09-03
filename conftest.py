import pytest
from api.api_helpers import ApiHelpers
from helpers.data_generator import get_order_data
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


