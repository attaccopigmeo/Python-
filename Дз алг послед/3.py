# алгоритм табулирования f(x) = x ** 2 + 5 на отрезке [a, b], шаг 1
a = int(input())
b = int(input())
for x in range(a, b + 1, 1):
    y = x ** 2 + 5
    print(x, y)