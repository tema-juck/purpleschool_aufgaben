from sys import argv as action

books: dict[str, str] = {}

books["Оно"] = "Стивен кинг"
books["Оно 2"] = "Стивен кинг"
books["Мертвые души"] = "Гоголь"
books["ЦЦЦ"] = "Анна"
books["ББББ"] = "Юра"


if action[1] == "filter":
    fillterd = list(filter(lambda book: books[book] == action[2], books))
    mapped = map(lambda book: f"{book} - {books[book]}", fillterd)
    print(*mapped, sep="\n")

if action[1] == "sort":
    if action[2] == "author":
        fillterd = sorted(books.items(), key=lambda book: book[1])
        mapped = map(lambda book: f"{book[1]} - {book[0]}", fillterd)
        print(*mapped, sep="\n")

    if action[2] == "book":
        fillterd = list(sorted(books.keys()))
        mapped = map(lambda book: f"{book} - {books[book]}", fillterd)
        print(*mapped, sep="\n")
