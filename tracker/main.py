from shlex import split
from commands.help import help_command
from commands.add import add_command
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
                    pass
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
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
    # r - read
    # w - write
    # a - append
    # x - make new file
    # b - binary file
    # t - text file
    # + - open to write/read
    # with open("notes.txt", "w", encoding="utf-8") as file:
    #     file.write("HI\n")

    # res = json.dumps(
    #     {
    #         "a": True,
    #         "b": [1, 2, 3]
    #     }
    # )

    # with open("tasks.json", "w", encoding="utf-8") as file:
    #     json.dump({
    #         "id": 1, "title": "Task 1"
    #     }, file, ensure_ascii=False, indent=2)

    # with open("tasks.txt", "r", encoding="utf-8") as f:
    #     for line in f:
    #         print(">", line.strip())

    # with open("tasks.json", "r", encoding="utf-8") as f:
    #     data = json.load(f)
    #     print(data)
    main()
