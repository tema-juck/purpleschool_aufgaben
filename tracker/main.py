from shlex import split
from commands.help import help_command
from commands.tasks import make_task
from helpers.args import parse_add


def main():
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
                    title, prio, due, tags = parse_add(args)
                    print(make_task(1, title, prio, tags, due))
                case "list":
                    pass
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
                case "exit":
                    break
                case _:
                    print("Неизвестная команда!")
        except KeyboardInterrupt:
            print("\nНепредвиденное завершение...")
            break
        except (ValueError, IndexError, TypeError) as e:
            print(f"[ERROR]: {e}")


if __name__ == "__main__":
    main()
