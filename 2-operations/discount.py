price = input("Введите цену товара: ")
discount = input("Введите размер скидки в процентах: ")

discount_amount = int(price) * int(discount) / 100
final_price = int(price) - discount_amount

print(f"Сумма скидки: {discount_amount}")
print(f"Цена со скидкой: {final_price}")