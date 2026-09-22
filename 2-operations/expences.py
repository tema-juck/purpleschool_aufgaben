food = input("Введите бюджет на еду: ")
transport = input("Введите бюджет на транспорт: ")
activities = input("Введите бюджет на развлечения: ")

sum = int(food) + int(transport) + int(activities)
average = sum // 3

print(f"Общий бюджет: {sum}")
print(f"Средний бюджет: {average}")