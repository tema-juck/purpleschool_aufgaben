"""Модуль заказов и бизнес логика"""



from datetime import time, date
from typing import TypedDict

STATUS = {"new", "in_progress", "done", "cancelled"}

class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: set[str]
    created_at: tuple[date, time]
    due: str | None
    closed_at: tuple[date, time] | None


def create_order():
    pass


def list_orders():
    pass


def edit_order():
    pass


def remove_order():
    pass
