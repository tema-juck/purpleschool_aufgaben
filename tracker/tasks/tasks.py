""""Task Module"""

from datetime import date
from typing import TypedDict, Optional

PRIORITIES = {"low", "med", "high"}


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: Optional[list[str]]
    status: str
    due: Optional[date]


def make_task(
        id_: int, title: str, priority: str = "med",
        tags: Optional[list[str]] = None, due: Optional[date] = None) -> Task:
    if priority not in PRIORITIES:
        raise ValueError(f"Invalid priority: {priority}")

    task: Task = {
        "id": id_,
        "title": title.strip(),
        "priority": priority,
        "status": "new",
        "tags": tags,
        "due": due
    }

    return task


def remove_task(tasks: list[Task], task_id) -> bool:
    before_len = len(tasks)
    tasks[:] = list(filter(lambda t: t["id"] != task_id, tasks))
    return len(tasks) < before_len


def update_task(task: Task, **changes):
    if "title" in changes:
        title = str(changes["title"]).strip()
        if not title:
            raise ValueError("Title can't be empty!")
        task["title"] = title

    if "prio" in changes:
        prio = str(changes["prio"]).strip().lower()
        if prio not in PRIORITIES:
            raise ValueError("Wrong priority! Only low|med|high !")
        task["priority"] = prio

    if "due" in changes:
        due = changes["due"]
        if due is not None and not isinstance(due, date):
            raise TypeError("Field 'due' must be date or None!")
        task["due"] = due


def find_task(tasks: list[Task], id_: int) -> Optional[Task]:
    return next((t for t in tasks if t["id"] == id_), None)
