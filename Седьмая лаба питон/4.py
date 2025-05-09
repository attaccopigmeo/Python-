# Дана последовательность из N (1 ≤ N ≤ 100000) целых чисел и число K (|K| ≤ 100000).//
# Сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов вправо, //
# если K –положительное и влево, если отрицательное.//
# В данной задаче нельзя использовать дополнительные списки. Обратите внимание, что нужно//
# именно преобразовать имеющийся список и распечатать его целиком, а не создать новый, даже//
# назвав его тем же самым именем (это возможно в языке Python).
lst = list(map(int, input("Введите элементы списка от 1 до 100000 (через пробел): ").split()))
k = int(input("На сколько сдвинуть? "))
if k > 0: # Сдвигаем вправо
    for i in range(k): # k раз сдвигаем вправо на 1
        last = lst[-1] # Сохраняем последний элемент
        for j in range(len(lst) - 1, 0, -1): # Идем из конца в начало, поэтому -1
            lst[j] = lst[j - 1] # Заменяем каждый эл. предыдущим
        lst[0] = last # Ставим бывший последний эл. в начало
else: # Сдвигаем влево аналогично с поправками
    k = - k # Получаем модуль k
    for i in range(k):
        first = lst[0]
        for j in range(1, len(lst)):
            lst[j - 1] = lst[j]
        lst[-1] = first
print("Новый список: ", *lst)
# Tests
# Введите элементы списка от 1 до 100000 (через пробел): 1 2 6 8 1000 4
# На сколько сдвинуть? 2
# Новый список:  1000 4 1 2 6 8
# Введите элементы списка от 1 до 100000 (через пробел): 22 4 55 2 1 8
# На сколько сдвинуть? -1
# Новый список:  4 55 2 1 8 22
# Введите элементы списка от 1 до 100000 (через пробел): 15 13 11 7 9 1
# На сколько сдвинуть? 3
# Новый список:  7 9 1 15 13 11