from shlex import split
from commands.edit import edit_command
from commands.help import help_command
from commands.add import add_command
from commands.list import list_command
from commands.remove import remove_command
from commands.tags import tag_command
from storage.file import load_tasks, save_tasks


def main():
    file_path = "tasks.json"
    tasks, next_id = load_tasks(file_path)
    print("Task Manager. help - для справки")
    while True:
        try:
            raw = input("> ").strip()
            parts = split(raw)
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    help_command()
                case "add":
                    next_id = add_command(tasks, args, next_id)
                case "list":
                    list_command(tasks, args)
                case "remove":
                    remove_command(tasks, args)
                case "edit":
                    edit_command(tasks, args)
                case "tags":
                    tag_command(tasks, args)
                case "exit":
                    save_tasks(tasks, file_path)
                    break
                case _:
                    print("Неизвестная команда!")
        except KeyboardInterrupt:
            save_tasks(tasks, file_path)
            print("\nНепредвиденное завершение...")
            break
        except (ValueError, IndexError, TypeError) as e:
            save_tasks(tasks, file_path)
            print(f"[ERROR]: {e}")


if __name__ == "__main__":
    main()
