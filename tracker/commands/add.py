"""Add Command Module"""

from helpers.args import parse_add
from helpers.table import srtingify_table
from tasks.tasks import Task, make_task


def add_command(tasks: list[Task], args: list[str], next_id: int) -> int:
    try:
        title, prio, due, tags = parse_add(args)
        task = make_task(1, title, prio, tags, due)
        tasks.append(task)
        print("Добавлена задача")
        print(srtingify_table([task]))
        return next_id + 1
    except ValueError as e:
        print(f"ERROR: {e}")
        return next_id
