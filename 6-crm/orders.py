"""Модуль заказов и бизнес логика"""


from datetime import datetime
from typing import TypedDict

STATUS = {"new", "in_progress", "done", "cancelled"}


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: set[str]
    created_at: datetime
    due: datetime | None
    closed_at: datetime | None


def create_order(id_: int, title: str, amount: float, email: str,
                 tags: set[str], due: str | None) -> Order:
    due_datetime = datetime.fromisoformat(due) if due is not None else None
    new_order: Order = {
        "id": id_,
        "title": title.strip(),
        "amount": amount,
        "email": email,
        "status": "new",
        "tags": tags,
        "created_at": datetime.now(),
        "due": due_datetime,
        "closed_at": None
    }
    return new_order


def list_orders(order_list: list[Order]):
    for order_item in order_list:
        for key, value in order_item.items():
            if isinstance(value, datetime):
                value = value.strftime("%d.%m.%Y %H:%M")

            print(f"{key}: {value}")

        print()


def edit_order(
    id_: int,
    order_list: list[Order],
    title: str | None = None,
    amount: float | None = None,
    email: str | None = None,
    status: str | None = None,
    tags: set[str] | None = None,
    due: str | None = None
) -> None:

    for order in order_list:
        if order["id"] == id_:

            if title is not None:
                order["title"] = title.strip()

            if amount is not None:
                order["amount"] = amount

            if email is not None:
                order["email"] = email

            if status is not None:
                if status not in STATUS:
                    print("Некорректный статус")
                    return

                order["status"] = status

                if status in ("done", "cancelled"):
                    order["closed_at"] = datetime.now()

            if tags is not None:
                order["tags"] = tags

            if due is not None:
                order["due"] = datetime.fromisoformat(due)

            return

    print("Заказ не найден")


def remove_order(id_: int, order_list: list[Order]) -> None:
    for order_item in order_list:
        if order_item["id"] == id_:
            order_list.remove(order_item)
            return

    print("Заказ не найден")
