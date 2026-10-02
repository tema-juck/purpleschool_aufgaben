"""Validators and Parsing"""


from datetime import date, datetime


def parse_add(args: list[str]):
    if not args:
        raise ValueError(
            "Используйте: add --title amount= email= [due=] [tags=]")

    title = args[0]
    amount, email, due, tags = str, str, None, None
    for arg in args[1:]:
        if arg.startswith("amount="):
            amount = arg.split("=", 1)[1]
        elif arg.startswith("email="):
            email = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            due_str = arg.split("=", 1)[1]
            try:
                due = parse_date(due_str)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты {due_str}. Ожидали [due=YYYY-MM-DD]") from e
        elif arg.startswith("tags="):
            tags_str = arg.split("=", 1)[1]
            tags = tags_str.split(",")
    return title, amount, email, due, tags


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()


def validate_email(email: str) -> bool:
    email = email.strip()

    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    local_part, domain = email.split("@")

    if not local_part or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


def parse_list(args: list[str]) -> dict:
    params = {
        "overdue": False,
        "tag": None,
        "limit": None,
    }

    for arg in args:
        if arg == "overdue":
            params["overdue"] = True

        elif arg.startswith("tag="):
            params["tag"] = arg.split("=", 1)[1]

        elif arg.startswith("limit="):
            params["limit"] = int(arg.split("=", 1)[1])

    return params


def parse_edit(args: list[str]) -> tuple:
    if len(args) < 2:
        raise ValueError("Не достаточно аргументов!")

    order_id = 0
    try:
        order_id = int(args[0])
    except ValueError as e:
        raise ValueError("Неправильно указан ID!") from e

    changes = {}

    for arg in args[1:]:
        if arg.startswith("title="):
            changes["title"] = arg.split("=", 1)[1]
        if arg.startswith("amount="):
            changes["amount"] = arg.split("=", 1)[1]
        elif arg.startswith("email="):
            changes["email"] = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            due_str = arg.split("=", 1)[1]
            try:
                changes["due"] = parse_date(due_str)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты {due_str}. Ожидали [due=YYYY-MM-DD]") from e
    return (order_id, changes)
