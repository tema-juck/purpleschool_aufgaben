"""Module for args help"""


from datetime import date, datetime


def parse_list(args: list[str]):
    # if not args:
    #     raise ValueError(
    #         "Используйте: list [by=prio|due]")
    by = None
    for arg in args:
        if arg.startswith("by="):
            by = arg.split("=", 1)[1]
    return by


def parse_add(args: list[str]):
    if not args:
        raise ValueError(
            "Используйте: add <title> [prio=low|med|high] [due=YYYY-MM-DD] [tags=a,b,c]")

    title = args[0]
    prio, due, tags = "med", None, None
    for arg in args[1:]:
        if arg.startswith("prio="):
            prio = arg.split("=", 1)[1]
        elif arg.startswith("due="):
            due_str = arg.split("=", 1)[1]
            try:
                due = parse_date(due_str)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты {due_str}. Ожидали [due=YYYY-MM-DD]"
                ) from e
        elif arg.startswith("tags="):
            tags_str = arg.split("=", 1)[1]
            tags = tags_str.split(",")
    return title, prio, due, tags


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()
