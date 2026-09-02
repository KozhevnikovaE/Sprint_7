import pytest
from api.api_helpers import ApiHelpers
from helpers.data_generator import generate_random_string
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
    """Фикстура с динамическими данными для заказа"""
    return {
        "first_name": generate_random_string(8),
        "last_name": generate_random_string(8),
        "address": f"ул. {generate_random_string(10)}, д. {generate_random_string(2)}",
        "metro_station": str(generate_random_string(2)),
        "phone": f"+7 {generate_random_string(10)}",
        "rent_time": 5,
        "delivery_date": "2026-07-31",
        "comment": "Тестовый заказ"
    }
