books: dict[str, tuple[str, ...]] = {}

books["Стивен Кинг"] = ("Оно", "Оно 2")
books["Гоголь"] = ("Мертвые души",)

all_books = []

for value in books.values():
    all_books.append(value) # type: ignore

print(all_books) # type: ignore

unique_autors: set[str] = set()

for key in books:
    unique_autors.add(key)


print(unique_autors)
