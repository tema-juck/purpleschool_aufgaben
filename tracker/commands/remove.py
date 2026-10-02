"""Remove Command Module"""


from tasks.tasks import Task, remove_task


def remove_command(tasks: list[Task], args: list[str]):
    task_id = None
    try:
        task_id = int(args[0])
        if remove_task(tasks, task_id):
            print(f"Success! Task {task_id} deleted!")
        else:
            print(f"Proble,! Task {task_id} not deleted!")
    except ValueError as e:
        print(f"[ERROR]: it must be Int: {e}")
