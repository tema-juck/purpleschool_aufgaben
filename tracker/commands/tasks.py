""""Task Module"""

from typing import TypedDict

PRIORITIES = {"low", "med", "high"}


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: list[str]
    status: str


# make_task()
def make_task(id_: int, title: str, priority: str = "med", tags: list[str] | None = None) -> Task:
    if priority not in PRIORITIES:
        raise ValueError(f"Invalid priority: {priority}")

    task: Task = {
        "id": id_,
        "title": title.strip(),
        "priority": priority,
        "status": "new",
        "tags": [] if tags is None else tags
    }

    return task
