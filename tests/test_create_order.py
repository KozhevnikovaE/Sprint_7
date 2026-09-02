import pytest
import allure
from api.orders_api import OrdersAPI

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с разными комбинациями цветов')
    @pytest.mark.parametrize('color', [
        ["BLACK"],          # Только BLACK
        ["GREY"],           # Только GREY
        ["BLACK", "GREY"],  # Оба цвета
        None                # Без цвета
    ])
    def test_create_order_with_colors(self, generate_order_data, color):
        order_data = generate_order_data
        order_data["color"] = color  # ← УСЛОВИЕ УБРАНО!
        response = OrdersAPI.create_order(**order_data)
        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
        assert response.json()["track"] > 0
