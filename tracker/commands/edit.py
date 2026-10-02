"""Edit Command Module"""

from helpers.args import parse_edit
from helpers.table import srtingify_table
from tasks.tasks import Task, find_task, update_task


def edit_command(tasks: list[Task], args: list[str]):
    task_id, changes = parse_edit(args)
    task = find_task(tasks, task_id)
    if task is None:
        print("Task not found!")
        return
    update_task(task, **changes)
    print(srtingify_table([task]))
