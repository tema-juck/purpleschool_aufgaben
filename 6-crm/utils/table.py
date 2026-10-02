"""Module for table"""


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from orders import Order


def srtingify_table(orders: list[Order]):
    headers = ["id", "Название", "Кол-во", "Почта", "Статус",
               "Тэги", "Дата создания", "Дедлайн", "Завершена"]
    rows = []
    for order in orders:
        tags = ",".join(sorted(order["tags"])) if order["tags"] else "-"
        rows.append([
            str(order["id"]),
            order["title"],
            order["amount"],
            order["email"],
            order["status"],
            tags,
            order["created_at"].strftime("%Y-%m-%d %H:%M"),
            order["due"].strftime("%Y-%m-%d") if order["due"] else "-"
        ])

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, col in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(col)))

    def fmt_row(row):
        return " | ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(row))

    out = []
    out.append(fmt_row(headers))
    out.append("-+-".join("-" * w for w in col_widths))
    for row in rows:
        out.append(fmt_row(row))
    return "\n".join(out)
