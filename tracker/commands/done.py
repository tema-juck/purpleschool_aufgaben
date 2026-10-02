"""Add Command Module"""

from tasks.tasks import Task, find_task
from helpers.table import srtingify_table


def done_command(tasks: list[Task], args: list[str]):
    if not args:
        raise ValueError("Not enough args! Use: done <id>")

    try:
        task_id = int(args[0])
    except ValueError:
        print("[ERROR]Failed 'id' Task!")
        return

    task = find_task(tasks, task_id)
    if not task:
        print(f"Task {task_id} not found!")
        return

    if task["status"] == "new":
        task["status"] = "done"
    elif task["status"] == "done":
        task["status"] = "new"

    print(srtingify_table([task]))
