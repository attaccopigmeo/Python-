def fib(number): # Функция, находящая числа Фибоначчи
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)
    
print("Числа Фибоначчи:")
for i in range(1, 10):
    print(fib(i))


def fact(number): # Функция, находящая факториалы чисел
    if number == 0:
        return 1
    else:
        return fact(number - 1) * number


Sum = 0
for n in range(1, 10 + 1):
    Sum += fact(n)
print("\n")
print("Сумма факториалов:", Sum)