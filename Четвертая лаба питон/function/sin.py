# Описать функцию Sin1(x, ε) вещественного типа (параметры x, ε — вещественные, ε > 0),\\
# находящую приближенное значение функции sin(x): sin(x) = x − x^3/(3!) + x^5/(5!) − … + (−1)^n·x^(2·n + 1)/((2·n + 1)!) + … .
# В сумме учитывать все слагаемые, модуль которых больше ε. С помощью Sin1 найти\\
# приближенное значение синуса для данного x при шести данных ε.
def Sin1(x, e): # Находит приближенное значение sin(x)
    y = 0
    d = x
    i = 1
    while abs(d) > e: # abs() - модуль числа
        y += d
        d *= - x ** 2 / ((i + 1) * (i + 2))
        i += 2
    return y


x = float(input("Введите x: "))
for _ in range(6):
    e = float(input("Введите ε: "))
    print("Приближенное значение sin(x):", Sin1(x, e))
    
# Тесты
# Введите x: 5
# Введите ε: 1  
# Приближенное значение sin(x): -1.1336172989818825
# Введите ε: 0.1 
# Приближенное значение sin(x): -0.937584049020681
# Введите ε: 0.01
# Приближенное значение sin(x): -0.9609213406827288
# Введите ε: 0.001
# Приближенное значение sin(x): -0.9587763690226141
# Введите ε: 0.0001
# Приближенное значение sin(x): -0.9589331651965991
# Введите ε: 0.00001
# Приближенное значение sin(x): -0.9589331651965991