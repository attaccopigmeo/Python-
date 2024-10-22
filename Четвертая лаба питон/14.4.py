# В текстовом файле b.otr хранится описание N отрезков: в первой строке - количество\\
# отрезков N, в следующих N строках по 4 числа - координаты концов отрезков: сначала абсцисса\\
# и ордината первой точки, потом абсцисса и ордината второй точки. Определить наименьшую\\
# длину отрезка среди имеющихся. Для вычисления длины отрезка напишите и используйте функцию.
from math import sqrt


def Length(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Определение длины отрезка


f = open("b.otr.txt", "r")
N = int(f.readline())
ans = 10 ** 10
for i in range(1, N + 1):
    x1, y1, x2, y2 = map(float, f.readline().split()) # .split() разделяет по пробелам
    l = Length(x1, y1, x2, y2)
    if l < ans:
        ans = l
print("Наименьшая длина отрезка: ", ans)