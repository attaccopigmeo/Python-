n = int(input("Введите n (кол-во суммируемых): "))
x = int(input("Введите x: "))
Sum = 0.0
for i in range(0, n + 1):
    a = 1
    for _ in range(x):
        a = (- x) ** i / 3 ** i # чередуется знак, в знаменателе степени тройки
    Sum += a
print("Сумма: ", Sum)