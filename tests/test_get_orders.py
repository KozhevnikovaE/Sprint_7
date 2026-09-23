import allure
from api.orders_api import OrdersAPI
from config import ERROR_MESSAGES

@allure.feature('Список заказов')
class TestGetOrders:
    
    @allure.title('В тело ответа возвращается список заказов')
    def test_get_orders_returns_list(self):
        response = OrdersAPI.get_orders()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
        
        response_data = response.json()
        assert "pageInfo" in response_data
        assert "availableStations" in response_data
        
        page_info = response_data["pageInfo"]
        assert "page" in page_info
        assert "total" in page_info
        assert "limit" in page_info

    @allure.title('Список заказов можно отфильтровать по курьеру')
    def test_get_orders_with_courier_filter(self):
        response_filtered = OrdersAPI.get_orders(courier_id=999999)
        assert response_filtered.status_code == 404
        assert ERROR_MESSAGES["courier_not_found_by_id"] in response_filtered.json()["message"]