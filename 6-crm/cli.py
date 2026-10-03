"""CLI Tool Command"""


from shlex import split

import orders as orders_
from storage import load_orders, save_orders
from utils.validators import parse_edit
from utils.table import srtingify_table


def cli_command():
    file_path = "orders.json"
    orders, next_id = load_orders(file_path)
    print("CRM Manager. help - для справки")
    while True:
        try:
            raw = input("> ").strip()
            parts = split(raw)
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    help_command()
                case "list":
                    list_command(orders, args)
                case "add":
                    next_id = add_command(orders, args, next_id)
                case "remove":
                    remove_command(orders, args)
                case "edit":
                    edit_command(orders, args)
                case "tags":
                    tags_command(orders, args)
                case "status":
                    status_command(orders, args)
                case "exit":
                    save_orders(orders, file_path)
                    print("Вы покинули программу!")
                    break
                case _:
                    print("Неизвестная команда!")
        except KeyboardInterrupt:
            save_orders(orders, file_path)
            print("\nНепредвиденное завершение...")
            break
        except (ValueError, IndexError, TypeError) as e:
            save_orders(orders, file_path)
            print(f"[ERROR]: {e}")


def help_command():
    """Help Command Module"""

    print("""Команды:
    list --overdue --tag=<tag> --limit=<N> -> Показать список
    add --title --amount --email [--due] [--tags] -> Добавить заказ
    remove --id <uuid> -> Удалить заказ
    edit --id [title=...] [amount=...] [email=...] [due=...] -> Изменить информацию заказа
    tags --id <uuid> [add|remove] <tag> -> удалить/добавить тэг
    status --id <uuid> statu=... - Выполнить
    help -> Помощь
    exit -> Выход
""")


def list_command(orders: list[orders_.Order], args: list[str]):
    orders_.list_orders(orders, args)


def add_command(orders: list[orders_.Order], args: list[str], next_id: int) -> int:
    return orders_.add_order(orders, args, next_id)


def remove_command(orders: list[orders_.Order], args: list[str]):
    try:
        if len(args) != 2:
            raise ValueError("Используйте: remove --id <число>")

        if args[0] != "--id":
            raise ValueError(f"Неизвестный флаг: {args[0]}")

        order_id = int(args[1])

        if orders_.remove_order(orders, order_id):
            print(f"Успех! Товар {order_id} удален!")
        else:
            print(f"Неудача! Товар {order_id} не найден!")

    except ValueError as e:
        print(f"[ERROR]: {e}")


def edit_command(orders: list[orders_.Order], args: list[str]):
    try:
        order_id, changes = parse_edit(args)

        order = orders_.find_order(orders, order_id)

        if order is None:
            print("Товар не найден!")
            return

        orders_.update_order(order, **changes)

        print("Товар обновлён!")
        print(srtingify_table([order]))

    except (ValueError, TypeError) as e:
        print(f"[ERROR]: {e}")


def tags_command(orders: list[orders_.Order], args: list[str]):
    try:
        if len(args) != 6:
            raise ValueError(
                "Use: tags --id <id> --action add|remove --tag <tag>"
            )

        order_id = None
        action = None
        tag = None

        i = 0

        while i < len(args):
            flag = args[i]
            value = args[i + 1]

            if flag == "--id":
                try:
                    order_id = int(value)
                except ValueError as e:
                    raise ValueError("ID must be a number") from e

            elif flag == "--action":
                action = value.lower()

            elif flag == "--tag":
                tag = value.lower().strip()

            else:
                raise ValueError(f"Unknown flag: {flag}")

            i += 2

        if order_id is None:
            raise ValueError("--id is required")

        if action not in {"add", "remove"}:
            raise ValueError("--action must be add or remove")

        if not tag:
            raise ValueError("--tag can't be empty")

        order = orders_.find_order(orders, order_id)

        if order is None:
            print(f"Order {order_id} not found!")
            return

        if action == "add":
            if order["tags"] is None:
                order["tags"] = set()

            order["tags"].add(tag)

        elif action == "remove":
            if order["tags"]:
                order["tags"].discard(tag)

        print(srtingify_table([order]))

    except ValueError as e:
        print(f"[ERROR]: {e}")


def status_command(orders: list[orders_.Order], args: list[str]):
    orders_.change_status(orders, args)
