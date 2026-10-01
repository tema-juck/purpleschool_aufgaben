"""Модуль работы с JSON"""

import json
from datetime import datetime
from orders import Order


def load_orders():
    try:
        with open("6-crm/orders.json", "r", encoding="utf-8") as file:
            pre_data = json.load(file)
            data: list[Order] = []
            for order in pre_data:
                order_data = order

                order_data["tags"] = set(order["tags"])
                order_data["created_at"] = datetime.fromisoformat(
                    order["created_at"])

                if order["due"] is not None:
                    order_data["due"] = datetime.fromisoformat(order["due"])

                if order["closed_at"] is not None:
                    order_data["closed_at"] = datetime.fromisoformat(
                        order["closed_at"])
                data.append(order_data)
            return data

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Ошибка: файл содержит некорректный JSON")
        return []


def save_orders(orders: list[Order]):
    try:
        data = []

        for order in orders:
            order_data = dict(order)

            order_data["tags"] = list(order["tags"])
            order_data["created_at"] = order["created_at"].isoformat()

            if order["due"] is not None:
                order_data["due"] = order["due"].isoformat()

            if order["closed_at"] is not None:
                order_data["closed_at"] = order["closed_at"].isoformat()

            data.append(order_data)

        with open("6-crm/orders.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    except json.JSONDecodeError as e:
        print(f"Ошибка: {e}")
