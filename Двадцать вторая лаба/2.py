"""Юный путешественник решил изучить схему авиационного сообщения Схема
авиационного сообщения задана в текстовом файле с именем FileName. в виде матрицы
смежности. Первая строка файла содержит количество городов (n) n<=25, связанных
авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить номера
городов, в которые из города K можно долететь менее чем с L пересадками. Перечислите
номера таких городов в порядке возрастания. Нумерация городов начинается с 1. Если
таких городов нет, выведите число (-1)."""

import matplotlib.pyplot as plt
import numpy as np


def draw_adjacency_matrix(adj_matrix):
    """
    Рисует граф по матрице смежности, используя только matplotlib.
    
    Параметры:
    adj_matrix : list of list или numpy.ndarray
        Квадратная матрица смежности (0 и 1 для невзвешенного графа)
    """
    if len(adj_matrix) != len(adj_matrix[0]):
        raise ValueError("Матрица смежности должна быть квадратной")
    
    n = len(adj_matrix)  # Количество вершин
    G = np.array(adj_matrix)
    
    # Создаем фигуру и оси
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Располагаем вершины на окружности
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    radius = 5
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    
    # Подписываем вершины
    for i in range(n):
        ax.text(x[i], y[i], str(i), ha='center', va='center', fontsize=12)
    
    # Рисуем рёбра (с учётом направленности)
    arrow_style = dict(arrowstyle='-', color='gray', lw=1.5)
    
    for i in range(n):
        for j in range(n):
            if G[i, j] != '0':  # Если есть ребро из i в j
                dx = x[j] - x[i]
                dy = y[j] - y[i]
                
                # Немного укорачиваем стрелку, чтобы она не перекрывала вершину
                start_x = x[i]
                start_y = y[i]
                end_x = x[j]
                end_y = y[j]
                
                # Рисуем стрелку
                ax.annotate("", xy=(end_x, end_y), xytext=(start_x, start_y), 
                            arrowprops=arrow_style)
    
    # Рисуем вершины (узлы)
    ax.scatter(x, y, s=500, c='skyblue', edgecolors='black', linewidths=1.5)
    
    plt.title("Граф по матрице смежности", pad=20)
    plt.tight_layout()
    plt.show()


filename = input('Введите FileName: ')
f = open('Двадцать вторая лаба/' + filename, 'r')
adj_matrix = []
n = int(f.readline())
for row in f:
    adj_matrix.append(list(row.split()))
f.close()

draw_adjacency_matrix(adj_matrix)

l = int(input('Введите максимальное число пересадок L: '))
k = int(input('Введите начальный город K: '))

# Используем алгоритм поиска в ширину
# В каждой вершине добавляем её непосещённых соседей в очередь
# Посещаем вершины в порядке очереди, при этом присваивая расстояние
# Если расстояние оказалось равно L, останавливаем поиск

queue = [(k - 1, 0)] # в очереди храним пары (номер города с 0, расстояние от K)
visited = [False] * n
ans = []
while len(queue) > 0:
    cur, dist = queue[0]
    if dist == l: # по построению алгоритма поиска в ширину далее все расстояния будут не меньше L
        break
    ans.append(cur + 1) # если расстояние меньше L, добавляем очередной город
    queue = queue[1:] # удаляем первый элемент
    for j in range(n):
        if adj_matrix[cur][j] != '0' and not visited[j]:
            queue.append((j, dist + 1))
print('Номера городов, которые можно достичь из города K менее, чем за L пересадок:')
if len(ans) > 0:
    print(*sorted(ans))
else:
    print(-1)