"""Генератор паролей"""
import random
import string
import sys

passwords: dict[str, str] = {}
# key -> str, pass -> str


def get_password() -> str:
    password = input("Ваш пароль: ")

    if password == "":
        password = generate_password()

    return password


def generate_password(length: int = 8, use_symbols: bool = True):
    if length < 3:
        return ""
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%&*?"
    pool = letters + numbers + symbols if use_symbols else letters + numbers
    password_chars: list[str] = []

    while len(password_chars) < length:
        password_chars.append(random.choice(pool))

    return "".join(password_chars)


def add_password():
    domain = input("Ваш домен: ")
    password = get_password()

    passwords[domain] = password


def show_passwords():
    print("Key".ljust(20), " | ", "Value")
    print("-" * 40)

    for key, value in passwords.items():
        print(key.ljust(20), " | ", value)
        print("-" * 40)


def delete_password():
    user_domain = input("Введите ваш домен: ")
    if user_domain not in passwords:
        print("Такого имени нет!")
        return

    passwords.pop(user_domain, None)
    print("Пароль удалён!")


def update_password():
    user_domain = input("Введите ваш домен: ")
    user_pass = get_password()

    if user_pass == "":
        user_pass = generate_password()

    if user_domain in passwords:
        passwords[user_domain] = user_pass
        print("Пароль обновлён!")
    else:
        print("Такого имени нет!")


def show_menu():
    print("1. Показать пароль")
    print("2. Добавить пароль")
    print("3. Удалить пароль")
    print("4. Обновить пароль")
    print("5. Выход")

    user_select = input("Ваш выбор: ")
    match user_select:
        case "1":
            show_passwords()
        case "2":
            add_password()
        case "3":
            delete_password()
        case "4":
            update_password()
        case "5":
            print("Bye!")
            sys.exit(0)
        case _:
            sys.exit(0)


while True:
    show_menu()
