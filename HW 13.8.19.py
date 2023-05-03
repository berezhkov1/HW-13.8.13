quantity = int(input("Введите количество билетов:"))
pay = 0
for i in range(1, quantity+1):
    print("Введите возраст", i, "посетителя:")
    age = int(input())
    if age < 18:
        pay += 0
    if 18 <= age < 25:
        pay += 990
    if age >= 25:
        pay += 1390
if quantity > 3:
    print("Сумма для заказа билетов:", int(pay*0.9), "рублей.")
else:
    print("Сумма для заказа билетов:", pay, "рублей")
