import random
import string

def generate_random_string(length=10):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_order_data():
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

