import allure
import requests
from config import BASE_URL

class OrdersAPI:
    @staticmethod
    @allure.step("Создание заказа для {first_name} {last_name}")
    def create_order(first_name, last_name, address, metro_station, phone,
                     rent_time, delivery_date, comment, color=None):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }
        if color:
            payload["color"] = color
        return requests.post(f'{BASE_URL}/api/v1/orders', json=payload)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders(courier_id=None, nearest_station=None, limit=30, page=0):
        params = {"limit": limit, "page": page}
        if courier_id:
            params["courierId"] = courier_id
        if nearest_station:
            params["nearestStation"] = nearest_station
        return requests.get(f'{BASE_URL}/api/v1/orders', params=params)