"""Модуль работы с JSON"""

from datetime import date, datetime
import json
# from datetime import datetime
from orders import Order


def load_orders(path: str) -> tuple[list[Order], int]:
    raw = {}
    try:
        with open(path, "r", encoding="utf-8") as file:
            raw = json.load(file)
    except FileNotFoundError:
        return [], 1
    except json.JSONDecodeError as e:
        print(f"Ошибка: файл содержит некорректный JSON {path}: {e}")

    orders: list[Order] = []
    max_id = 0

    for item in raw.get("orders", []):
        try:
            order: Order = {
                "id": int(item["id"]),
                "title": item["title"],
                "amount": float(item["amount"]),
                "email": item["email"],
                "status": item["status"],
                "tags": set(item.get("tags") or []),
                "created_at": datetime.fromisoformat(
                    item["created_at"]
                ),
                "due": (
                    date.fromisoformat(item["due"])
                    if item.get("due")
                    else None
                ),
                "closed_at": (
                    datetime.fromisoformat(item["closed_at"])
                    if item.get("closed_at")
                    else None
                ),
            }
            orders.append(order)
            max_id = max(max_id, int(item["id"]))
        except (KeyError, TypeError, ValueError) as e:
            print(f"[WARN] Miss the Order: {e}")
    return orders, max_id + 1


def save_orders(orders: list[Order], path: str):
    data = {
        "orders": [
            {
                "id": order["id"],
                "title": order["title"],
                "amount": order["amount"],
                "email": order["email"],
                "status": order["status"],
                "tags": list(order["tags"]) if order["tags"] is not None else [],
                "created_at": order["created_at"].isoformat(),
                "due": order["due"].isoformat() if order["due"] is not None else None,
                "closed_at": (
                    order["closed_at"].isoformat()
                    if order["closed_at"] is not None
                    else None
                ),
            }
            for order in orders
        ]
    }

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
