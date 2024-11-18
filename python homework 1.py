from math import sqrt

print('Вычислим деление -5 на 3')
a1 = -5
b1 = 3
print(a1, "/", b1, "=", a1 / b1)
print()

print('Вычислим деление 5 на -3')
a2 = 5
b2 = -3
print(a2, "/", b2, "=", a2 / b2)
print()

print('Вычислим деление -5 на -3')
a3 = -5
b3 = -3
print(a3, "/", b3, "=", a3 / b3)
print()

print('Решим квадратное уравнение ax^2 + bx + c')
# В задаче необходимо учитывать, что дискриминант может равняться нулю или отрицательному числу
a = int(input('Введите первый коэффициент: '))
b = int(input('Введите второй коэффициент: '))
c = int(input('Введите третий коэффициент: '))
print('Вычислим дискриминант')
D = b^2 - 4 * a * c
print('D = b^2 - 4 * a * c = ', D)
if D > 0:
    x1 = ((-b) + sqrt(D)) / (2 * a)
    x2 = ((-b) - sqrt(D)) / (2 * a)
    print('Корни уравнения: ', x1, x2)
elif D == 0:
    x = (-b) / (2 * a) 
    print('Дискриминант равен нулю, следовательно у уравнения один корень: ', x)
else:
    print('Уравнение не имеет действительных корней')
print()

print('Найдем периметр и площадь прямоугольника')
n = int(input('Введите ширину прямоугольника: '))
m = int(input('Введите длину прямоугольника: '))
P = 2 * n + 2 * m
S = n * m
if n == m:
    print('Вы задали квадрат')
    print('Периметр Вашего квадрата: ', P)
    print('Площадь Вашего квадрата: ', S)
else:
    print('Периметр Вашего прямоугольника: ', P)
    print('Площадь Вашего прямоугольника: ', S)
print()