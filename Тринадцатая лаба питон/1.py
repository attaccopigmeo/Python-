"""
Археолог нашел N артефактов. Известны веса (сi) и объемы (di) артефактов. Нужно
выбрать такое подмножество найденных вещей, чтобы суммарный их вес не превысил B кг, но
был наиболее близок к B, а количество взятых артефактов было как можно больше. Известно,
что решение единственно. Укажите порядковые номера вещей, которые надо взять. Исходные
данные находятся в текстовом файле, в первой строке указаны N и B, а во второй строке
значения весов (в кг), в третьей объемы находок (в куб.см). Вывести так же суммарный вес и
суммарный объем результата.
"""
f = open("Тринадцатая лаба питон/1.txt", "r")
N, B = map(int, f.readline().split())
c = list(map(int, f.readline().split()))
d = list(map(int, f.readline().split()))
f.close()

# Создаем таблицу мемоизации
dp = [[0 for _ in range(B + 1)] for _ in range(N + 1)]
# эл-т dp[i][j] соответствует ценности, полученной, если мы взяли элементы с номерами меньше i при ограничении веса j
for i in range(1, N + 1):
    for j in range(1, B + 1):
        if c[i - 1] <= j: # Вес текущего элемента меньше или равен текущему максимальному
            # пробуем повысить объем, добавив элемент i
            # либо мы оставляем состав рюкзака как был,
            # либо добавляем элемент, отнимая место у остальных
            dp[i][j] = max(dp[i - 1][j], 1 + dp[i - 1][j - c[i - 1]])
            # d[i - 1] + dp[i - 1][j - c[i - 1]] - объем, если мы добавили элемент (при этом отняв вес этого элемента)
            # dp[i - 1][j] - объем, если мы не добавляли элемент
            # max() - чтобы выбрать из них больший по объему
# восстанавливаем список элементов: мы взяли элемент i, если в текущей ячейке значение больше, чем в предыдущей
i = N
j = B
res = []
w = 0
v = 0
while dp[i][j] > 0:
    if dp[i][j] != dp[i - 1][j]:
        res.append(i)
        w += c[i - 1]
        v += d[i - 1]
        j -= c[i - 1]
    i -= 1
print("Порядковые номера вещей:", *res)
print("Суммарные вес и объем вещей:", w, v)
# Чтение данных из файла (без try)
file_path = 'Тринадцатая лаба питон/1.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

# Парсим первую строку (N и B)
N, B = map(int, lines[0].split())

# Парсим веса и объемы
weights = list(map(int, lines[1].split()))
volumes = list(map(int, lines[2].split()))

# Таблица для динамического программирования
# dp[w] хранит максимальный объем для веса w
dp = [[0] * (B + 1) for _ in range(N + 1)]
picked_items = [[[] for _ in range(B + 1)] for _ in range(N + 1)]

# Заполняем таблицу мемоизации
for i in range(1, N + 1):  # Для каждого артефакта
    for w in range(B + 1):  # Для каждого возможного веса
        # Если текущий артефакт не помещается в оставшийся вес
        if weights[i - 1] > w:
            dp[i][w] = dp[i - 1][w]
            picked_items[i][w] = picked_items[i - 1][w]
        else:
            # Оптимальное значение: взять или не взять текущий артефакт
            without_item = dp[i - 1][w]
            with_item = dp[i - 1][w - weights[i - 1]] + volumes[i - 1]

            if with_item > without_item:
                dp[i][w] = with_item
                picked_items[i][w] = picked_items[i - 1][w - weights[i - 1]] + [i - 1]
            else:
                dp[i][w] = without_item
                picked_items[i][w] = picked_items[i - 1][w]

# Ищем решение с максимальным объемом и весом, близким к B
best_weight = max(range(B + 1), key=lambda w: dp[N][w])
best_subset = picked_items[N][best_weight]

# Форматируем результат
result = {
    "indices": [i + 1 for i in best_subset],  # Переход к порядковым номерам
    "total_weight": sum(weights[i] for i in best_subset),
    "total_volume": dp[N][best_weight],
}
print(result)
