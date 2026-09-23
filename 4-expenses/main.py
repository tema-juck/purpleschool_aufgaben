# money = input("Введите сумму в рублях: ").lower().split()

# rub_list = ["руб", "рубль", "рубля", "рублей"]
# kop_list = ["коп", "копейка", "копейки", "копеек"]

# if len(money) == 2:
#     if money[0].isdigit() and money[1] in rub_list:
#         rubles = int(money[0])
#         print(f"{rubles}.00 ₽")
#     else:
#         print("Некорректный формат суммы")

# elif len(money) == 4:
#     if (money[0].isdigit()
#             and money[1] in rub_list
#             and money[2].isdigit()
#             and money[3] in kop_list):

#         rubles = int(money[0])
#         kopecks = int(money[2])

#         if kopecks <= 99:
#             print(f"{rubles}.{kopecks:02d} ₽")
#         else:
#             print("Некорректный формат суммы")

#     else:
#         print("Некорректный формат суммы")

# else:
#     print("Некорректный формат суммы")

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
    
    user_input = int(input("Введите номер меню: "))
    
    match user_input:
        case 4:
            print("Вы покинули программу!")
            break
        case _:
            break