

from orders import Order, create_order, list_orders
from storage import save_orders, load_orders

orders: list[Order] = []

order = create_order(
    1,
    "Name",
    3.0,
    "test@",
    {"1", "2"},
    None
)


orders.append(order)
list_orders(orders)

save_orders(orders)

order = load_orders()
print(order)
