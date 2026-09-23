money = input("Введите сумму в рублях: ").lower().strip()

name_list = ["руб", "коп", "рубль", "рубля", "рублей", "копейка", "копейки", "копеек"]

if  money.count("руб") != 1 or money.count("коп") != 1:
    print("Некорректный формат суммы")
    exit()

rubles = money.split("руб")[0].strip()

kopecks = int(money.split("руб")[1].strip().split("коп")[0].strip())

if kopecks > 99:
    print("Некорректный формат суммы")
    exit()

if not rubles.isdigit():
    print("Некорректный формат суммы")
    exit()
else:
    print(f"{rubles}.{kopecks:02d} ₽")
    exit()