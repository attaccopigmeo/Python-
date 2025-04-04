# Дано целое число N и набор из N целых чисел. Найти максимальное количество
# подряд идущих минимальных элементов из данного набора.
# RECURSION
def max_of_min_numbers_in_set(N): # Функция, которая ищет максимальное количество
# подряд идущих минимальных элементов из данного набора
    x = int(input("Введите число: "))
    if N == 1:
        return x, 1, 1
    y, k, m = max_of_min_numbers_in_set(N - 1)
    if x < y:
        return x, 1, 1
    elif x == y:
        if k + 1 > m:
            return x, k + 1, k + 1
        else:
            return x, k + 1, m
    else:
        if k > m:
            return x, 0, k
        else:
            return x, 0, m
# Возвращает минимум, кол-во подряд идущих в текущей части и искомое в задаче


N = int(input("Введите, сколько чисел вы ходите задать: "))
_,_,ans = max_of_min_numbers_in_set(N) # Нам нужно только последнее
print("Максимальное кол-во мин. эл., идущих подряд: ", ans)
# Однопроходной алгоритм считывает свои входные данные один раз, путем обработки элементов по порядку
# Введите, сколько чисел вы ходите задать: 5
# Введите число: 1
# Введите число: 5
# Введите число: 1
# Введите число: 1
# Введите число: 5
# Максимальное кол-во мин. эл., идущих подряд:  2
# Введите, сколько чисел вы ходите задать: 7
# Введите число: 2
# Введите число: 2
# Введите число: 2
# Введите число: 7
# Введите число: 2
# Введите число: 2
# Введите число: 1
# Максимальное кол-во мин. эл., идущих подряд:  1
# Введите, сколько чисел вы ходите задать: 5
# Введите число: 2
# Введите число: 2
# Введите число: 2
# Введите число: 2
# Введите число: 9
# Максимальное кол-во мин. эл., идущих подряд:  4