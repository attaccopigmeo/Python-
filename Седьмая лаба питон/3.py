# Напишите программу, которая выбирает из списка все простые числа в другой список.//
# Если в исходном списке нет простых чисел, программа должна вывести число 0.
def is_prime(x):
    if x == 1:
        return False
    for d in range(2, x):
        if x % d == 0:
            return False
    return True


lst = list(map(int, input("Введите элементы списка (через пробел): ").split()))
lst1 = []
for i in lst:
    if is_prime(i): # Если ф-ция возвращает True, то добавляем простое число в список lst1
        lst1.append(i)
if len(lst1) == 0:
    print(0)
else:
    print("Список простых чисел: ", *lst1)