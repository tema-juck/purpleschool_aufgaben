"""Validators and Parsing"""


from datetime import date, datetime


def parse_add(args: list[str]):
    if not args:
        raise ValueError(
            "Используйте: add --title <название> --amount <сумма> "
            "--email <email> [--due YYYY-MM-DD] [--tags tag1,tag2]"
        )

    title = None
    amount = None
    email = None
    due = None
    tags = None

    i = 0

    while i < len(args):
        flag = args[i]

        if not flag.startswith("--"):
            raise ValueError(f"Ожидался флаг, получено: {flag}")

        if i + 1 >= len(args):
            raise ValueError(f"Для {flag} не указано значение")

        value = args[i + 1]

        if flag == "--title":
            title = value

        elif flag == "--amount":
            amount = value

        elif flag == "--email":
            email = value

        elif flag == "--due":
            try:
                due = parse_date(value)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты {value}. "
                    "Ожидали YYYY-MM-DD"
                ) from e

        elif flag == "--tags":
            tags = value.split(",")

        else:
            raise ValueError(f"Неизвестный флаг: {flag}")

        i += 2

    if title is None:
        raise ValueError("Не указан --title")

    if amount is None:
        raise ValueError("Не указан --amount")

    if email is None:
        raise ValueError("Не указан --email")

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
        if arg == "--overdue":
            params["overdue"] = True

        elif arg.startswith("--tag="):
            tag = arg.split("=", 1)[1].strip()

            if not tag:
                raise ValueError("--tag не может быть пустым")

            params["tag"] = tag

        elif arg.startswith("--limit="):
            value = arg.split("=", 1)[1]

            try:
                limit = int(value)
            except ValueError as e:
                raise ValueError("--limit должен быть числом") from e

            if limit <= 0:
                raise ValueError("--limit должен быть больше 0")

            params["limit"] = limit

        else:
            raise ValueError(f"Неизвестный аргумент: {arg}")

    return params


def parse_edit(args: list[str]) -> tuple[int, dict]:
    if len(args) < 4:
        raise ValueError(
            "Use: edit --id <id> "
            "[--title <title>] "
            "[--amount <amount>] "
            "[--email <email>] "
            "[--due YYYY-MM-DD]"
        )

    order_id = None
    changes = {}

    i = 0

    while i < len(args):
        flag = args[i]

        if i + 1 >= len(args):
            raise ValueError(f"No value for {flag}")

        value = args[i + 1]

        if flag == "--id":
            try:
                order_id = int(value)
            except ValueError as e:
                raise ValueError("ID must be a number") from e

        elif flag == "--title":
            changes["title"] = value

        elif flag == "--amount":
            changes["amount"] = value

        elif flag == "--email":
            changes["email"] = value

        elif flag == "--due":
            try:
                changes["due"] = parse_date(value)
            except ValueError as e:
                raise ValueError(
                    f"Wrong date format: {value}. Expected YYYY-MM-DD"
                ) from e

        else:
            raise ValueError(f"Unknown flag: {flag}")

        i += 2

    if order_id is None:
        raise ValueError("--id is required")

    if not changes:
        raise ValueError("Nothing to update")

    return order_id, changes
