# Вариант 14
# Данo натуральное число х, (10000 ≤ х ≤ 99999). Определить, верно ли, что все цифры числа различны между собой.\
    # Необходимо использовать логическую переменную, и в качестве результата вывести ее значение.
x = int(input("Введите число: "))
x >= 10000
x <= 99999
n = True
# Далее определяем различны ли все цифры числа x
while  x > 0:
    d1 = x % 10
    x = x // 10
    d2 = x % 10
    x = x // 10
    d3 = x % 10
    x = x // 10
    d4 = x % 10
    x = x // 10
    d5 = x % 10
    x = x // 10
n = (d1 != d2) and (d1 != d3) and (d1 != d4) and (d1 != d5) and (d2 != d3) and (d2 != d4) and (d2 != d5) and \
    (d3 != d4) and (d3 != d5) and (d4 != d5)
print("Различны ли все цифры числа x? ", n)

# input 12345, output True
# input 12342, output False
# input 24556, output False