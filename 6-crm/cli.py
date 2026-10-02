"""CLI Tool Command"""


from shlex import split

import orders as orders_
from storage import load_orders, save_orders
from utils.validators import parse_edit


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
                    next_id -= 1
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
    order_id = None
    try:
        order_id = int(args[0])
        if orders_.remove_order(orders, order_id):
            print(f"Успех! Товар {order_id} удален!")
        else:
            print(f"Неудача! Товар {order_id} не удален!")
    except ValueError as e:
        print(f"[ERROR]: ID должно быть числом: {e}")


def edit_command(orders: list[orders_.Order], args: list[str]):
    order_id, changes = parse_edit(args)
    order = orders_.find_order(orders, order_id)
    if order is None:
        print("Товар не найден!")
        return
    orders_.update_order(order, **changes)


def tags_command(orders: list[orders_.Order], args: list[str]):
    if len(args) < 3:
        raise ValueError("Not enough args! Use: tags <id> add|remove <tag>")

    try:
        order_id = int(args[0])
    except ValueError:
        print("[ERROR]Failed 'id' Task!")
        return

    action = args[1].lower()
    tag = args[2].lower().strip()

    order = orders_.find_order(orders, order_id)
    if not order:
        print(f"Order {order_id} not found!")
        return

    if action == "add":
        if not order["tags"]:
            order["tags"] = {tag}
            return
        if tag not in order["tags"]:
            order["tags"].add(tag)
            return

    if action == "remove":
        if not order["tags"]:
            return
        try:
            order["tags"].remove(tag)
        except ValueError:
            pass


def status_command(orders: list[orders_.Order], args: list[str]):
    orders_.change_status(orders, args)
