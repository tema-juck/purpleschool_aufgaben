money = input("Введите сумму в рублях: ").lower().strip()

rubles = money.split("руб")[0].strip()
kopecks = money.split("руб")[1].strip().split("коп")[0].strip()

if not rubles.isdigit() or (kopecks and not kopecks.isdigit()):
    print("Некорректный формат суммы")
else:
    print(f"{rubles}.{kopecks.zfill(2)} ₽")