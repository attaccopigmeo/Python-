# Дан произвольный список. Не изменяя его и не используя дополнительные списки,//
# определите, какое число в этом списке встречается чаще всего.
lst = list(map(int, input("Введите элементы списка (через пробел): ").split()))
min_int = 0
max_int = 0
for i in lst: # Перебираем список, определяем диапазон чисел
    if i < min_int:
        min_int = i
    if i > max_int:
        max_int = i
ans = 0
max_cnt = 0 # Сколько раз встретилось самое частое число
for i in range(min_int, max_int + 1): # Считаем, сколько раз встречается каждое число из диапазона по очереди
    cnt = 0 # Счетчик текущего числа
    for j in lst:
        if j == i:
            cnt += 1
    if cnt > max_cnt:
        ans = i
        max_cnt = cnt
    if cnt == 1:
        max_cnt = 0
if max_cnt == 0:
    print("Все числа встречаются единожды")
else:
    print("Число, встречающееся чаще всего:", ans)
# Тесты
# Введите элементы списка (через пробел): 1 2 3 4 6
# Все числа встречаются единожды
# Введите элементы списка (через пробел): 1 22 4 5 22 6
# Число, встречающееся чаще всего: 22
# Введите элементы списка (через пробел): 1 22 3 22 1 4 22
# Число, встречающееся чаще всего: 22