# Дано целое число N и набор из N вещественных чисел. Вывести сумму и произведение \
    # чисел из данного набора.
N = int (input("Введите целое число N: "))
Sum = 0.0
Prod = 1.0
for _ in range(N):
    x = float(input("Введите числа (по одному в строке):"))
    Sum += x
    Prod *= x
print (Sum, Prod)
# Тесты
# input 3, 1, 2, 3, output 6.0, 6.0
# input 4, 4, 7, 9, 1 output 21.0, 252.0
# input 3, 2.5, 5.1, 9.3 output 16.9, 118.575