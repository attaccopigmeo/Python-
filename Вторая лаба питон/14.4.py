# Даны натуральные числа n и k. Найти значение выражения: 1^k+2^k+3^k+...+n^k.\ 
# Результат вывести в виде вещественного числа.
n = int(input("Введите n: "))
k = int(input("Введите k: "))
Sum = 0.0
for i in range(n):
    Sum += i ** k
print("Сумма: ", Sum)
# Тесты
# input 2, 1 output 1.0
# input 5, 6 output 4890.0
# input 6, 3 output 225.0