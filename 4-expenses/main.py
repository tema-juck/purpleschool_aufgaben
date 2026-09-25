expences: list[float] = []

total = 0
average = 0

RUB_LIST = ["руб", "рубль", "рубля", "рублей"]
KOP_LIST = ["коп", "копейка", "копейки", "копеек"]


def add_expense(exp: list[float], value: float) -> list[float]:
    exp.append(value)
    return exp


def delete_expence(exp: list[float], idx: int):
    exp.pop(idx)


def get_total(exp: list[float]):
    return sum(exp)


def get_average(exp: list[float]):
    return sum(exp) / len(exp)


def print_report(exp: list[float]):

    print("=" * 30)
    print(f"Все ваши расходы : {exp}\n")
    print("=" * 30)


def parse_expences(input_user: str):
    money = input_user.lower().split()

    if len(money) == 2:
        if money[0].isdigit() and money[1] in RUB_LIST:
            return int(money[0])

    elif len(money) == 4:
        if (money[0].isdigit()
                and money[1] in RUB_LIST
                and money[2].isdigit()
                and money[3] in KOP_LIST
                and int(money[2]) <= 99):

            return f"{int(money[0])}.{int(money[2]):02d} "

    print("Некорректный формат суммы")
    return ""


    # Menu
MENU = (
    "1. Добавить расход",
    "2. Показать все расходы",
    "3. Показать сумму и средний расход",
    "4. Удалить расход по номеру",
    "5. Выход"
)


while True:
    for option in MENU:
        print(option + "\n")

    user_input = input("Введите номер меню: ")

    match user_input:
        case "1":
            user_money = input("\nВведите сумму в рублях: ")
            parse_user_money = float(parse_expences(user_money))
            add_expense(expences, parse_user_money)
        case "2":
            print_report(expences)
        case "3":
            total = get_total(expences)
            average = get_average(expences)
            print(f"\nВаша сумма рассходов: {total}\n")
            print(f"Ваш средний рассход: {average}\n")
        case "4":
            index = int(input("\nВведите индекс элемента (от 0): "))
            delete_expence(expences, index)
        case "5":
            print("\nВы покинули программу!")
            break
        case _:
            print("\nТакого пункта нет, попробуйте ещё раз!\n")
