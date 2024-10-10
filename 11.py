from math import log2, ceil
# лист
a = int(input())
b = int(input())
# конверт
c = int(input())
d = int(input())
# a / c = 2 ** n, n - кол-во раз сколько надо сложить лист вдоль a
# ceil - округление вверх
# n = ceil(log2(a / c)) + ceil(log2(b / d)) - эффективный вариант
n = 0
while a > c:
    n += 1
    a = a / 2
while b > d:
    n += 1
    b = b / 2
print(n)