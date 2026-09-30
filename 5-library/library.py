from sys import argv as action


class LibraryError(BaseException):
    pass


class InvalidFilterError(LibraryError):
    pass


class InvalidCommandError(LibraryError):
    pass


class InvalidParamError(LibraryError):
    pass


books: dict[str, str] = {}

books["Оно"] = "Стивен кинг"
books["Оно 2"] = "Стивен кинг"
books["Мертвые души"] = "Гоголь"
books["ЦЦЦ"] = "Анна"
books["ББББ"] = "Юра"


try:
    if action[1] == "filter":
        if len(action) < 3:
            raise InvalidFilterError("Не передан текст фильтра")

        filtered = filter(
            lambda book: books[book] == action[2],
            books
        )

        mapped = map(
            lambda book: f"{book} - {books[book]}",
            filtered
        )

        print(*mapped, sep="\n")

    elif action[1] == "sort":
        if len(action) < 3:
            raise InvalidParamError("Не передан параметр сортировки")

        if action[2] not in ("author", "book"):
            raise InvalidParamError(
                "Передан неправильный параметр сортировки!"
            )

        if action[2] == "author":
            sorted_books = sorted(
                books.items(),
                key=lambda book: book[1]
            )

            mapped = map(
                lambda book: f"{book[0]} - {book[1]}",
                sorted_books
            )

        elif action[2] == "book":
            sorted_books = sorted(books.keys())

            mapped = map(
                lambda book: f"{book} - {books[book]}",
                sorted_books
            )

        print(*mapped, sep="\n")

    else:
        raise InvalidCommandError("Некорректная команда!")

except InvalidFilterError as e:
    print(f"Ошибка: {e}")
except InvalidCommandError as e:
    print(f"Ошибка: {e}")
except InvalidParamError as e:
    print(f"Ошибка: {e}")
