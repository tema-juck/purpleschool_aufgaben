"""Модуль заказов и бизнес логика"""


from datetime import date, datetime
from typing import Optional, TypedDict

from utils.table import srtingify_table
from utils.validators import parse_list, parse_add, validate_email

STATUS = {"new", "in_progress", "done", "cancelled"}


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: Optional[set[str]]
    created_at: datetime
    due: date | None
    closed_at: datetime | None


def create_order(id_: int, title: str, amount: float, email: str,
                 tags: set[str] | None, due: str | None) -> Order:
    due_datetime = date.fromisoformat(due) if due is not None else None
    new_order: Order = {
        "id": id_,
        "title": title.strip(),
        "amount": amount,
        "email": email,
        "status": "new",
        "tags": tags,
        "created_at": datetime.today(),
        "due": due_datetime,
        "closed_at": None
    }
    return new_order


def list_orders(orders: list[Order], args: list[str]):
    try:
        subset = orders[:]
        params = parse_list(args)

        if params["overdue"]:
            subset = [
                order
                for order in subset
                if order["due"] is not None
                and order["due"] < date.today()
            ]

            subset = sorted(
                subset,
                key=lambda order: order["due"] or date.max
            )

        if params["tag"] is not None:
            subset = [
                order
                for order in subset
                if order["tags"] is not None
                and params["tag"] in order["tags"]
            ]

        if params["limit"] is not None:
            subset = subset[:params["limit"]]

        if not subset:
            print("Список пустой!")
            return

        print(srtingify_table(subset))

    except ValueError as e:
        print(f"[ERROR]: {e}")


def add_order(orders: list[Order], args: list[str], next_id: int) -> int:
    try:
        title, amount, email, due, tags = parse_add(args)
        if not isinstance(amount, str):
            raise ValueError("Сумма должна быть строкой")
        if not isinstance(email, str):
            raise ValueError("Email должен быть строкой")
        if not validate_email(email):
            raise ValueError("Некорректный email")
        if tags is not None:
            tags = set(tags)
        order = create_order(
            next_id,
            title,
            float(amount),
            email,
            tags,
            due.isoformat() if due is not None else None,
        )
        orders.append(order)
        print("Добавлена задача")
        print(srtingify_table([order]))
        return next_id + 1
    except ValueError as e:
        print(f"ERROR: {e}")
        return next_id


def remove_order(orders: list[Order], order_id: int) -> bool:
    before_len = len(orders)

    orders[:] = [
        order
        for order in orders
        if order["id"] != order_id
    ]

    return len(orders) < before_len


def update_order(order: Order, **changes):
    if "title" in changes:
        title = str(changes["title"]).strip()
        if not title:
            raise ValueError("Title can't be empty!")
        order["title"] = title

    if "amount" in changes:
        amount = str(changes["amount"]).strip()
        if not amount:
            raise ValueError("Amount can't be empty!")
        order["amount"] = float(amount)

    if "email" in changes:
        email = str(changes["email"]).strip()

        if not email:
            raise ValueError("Email can't be empty!")

        if not validate_email(email):
            raise ValueError("Invalid email!")

        order["email"] = email

    if "due" in changes:
        due = changes["due"]
        if due is not None and not isinstance(due, date):
            raise TypeError("Field 'due' must be date or None!")
        order["due"] = due


def find_order(orders: list[Order], id_: int) -> Optional[Order]:
    return next((o for o in orders if o["id"] == id_), None)


def change_status(orders: list[Order], args: list[str]):
    try:
        if len(args) != 4:
            raise ValueError(
                "Используйте: status --id <id> --status <status>"
            )

        order_id = None
        new_status = None

        i = 0

        while i < len(args):
            flag = args[i]
            value = args[i + 1]

            if flag == "--id":
                try:
                    order_id = int(value)
                except ValueError as e:
                    raise ValueError("ID должно быть числом") from e

            elif flag == "--status":
                new_status = value

            else:
                raise ValueError(f"Неизвестный флаг: {flag}")

            i += 2

        if order_id is None:
            raise ValueError("Не указан --id")

        if new_status is None:
            raise ValueError("Не указан --status")

        order = find_order(orders, order_id)

        if order is None:
            print(f"Task {order_id} not found!")
            return

        order["status"] = new_status

        print(srtingify_table([order]))

    except ValueError as e:
        print(f"[ERROR]: {e}")
