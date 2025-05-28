"""Юный путешественник решил изучить схему авиационного сообщения Схема
авиационного сообщения задана в текстовом файле с именем FileName1. в виде матрицы
смежности. Первая строка файла содержит количество городов (n) n<=15, связанных
авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить сколько
есть маршрутов из города К1 в город К2 с L пересадками. В файл с именем FileName2 в
первой строке выведите число таких маршрутов, а в следующих строках перечислите все
такие маршруты в лексикографическом порядке. Маршрут задается перечислением
номеров городов, нумерация городов идет с 1. Если таких маршрутов нет, выведите число
(-1)."""

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


# Алгоритм поиска в глубину
# Возвращает список маршрутов
def dfs(n, adj_matrix, k1, k2, l, cur = None, dist = -1):
    # по умолчанию cur = k1
    if cur is None:
        cur = k1
    # условие остановки рекурсии: достигли K2 за L пересадок
    if cur == k2 and dist == l:
        return [[k2 + 1]] # возвращаем один маршрут из текущего-конечного элемента
    if dist > l:
        return [] # если сделали больше L пересадок, маршрут не подходит, не возвращаем ничего
    routes = []
    # перебираем все вершины
    for j in range(n):
        if adj_matrix[cur][j] == '0':
            continue
        # если нашлось ребро - пробуем пройти по нему и построить маршруты
        new_routes = dfs(n, adj_matrix, k1, k2, l, j, dist + 1)
        for new_route in new_routes:
            routes.append([cur + 1] + new_route) # добавляем к каждому маршруту в начало текущий элемент и добавляем маршрут в список
    return routes


filename = input('Введите FileName1: ')
f1 = open('Двадцать вторая лаба/' + filename, 'r')
adj_matrix = []
n = int(f1.readline())
for row in f1:
    adj_matrix.append(list(row.split()))
f1.close()

draw_adjacency_matrix(adj_matrix)

l = int(input('Введите нужное число пересадок L: '))
k1 = int(input('Введите начальный город K1: '))
k2 = int(input('Введите конечный город K2: '))

routes = dfs(n, adj_matrix, k1 - 1, k2 - 1, l)

filename = input('Введите FileName2: ')
f2 = open('Двадцать вторая лаба/' + filename, 'w')
f2.write(f'{len(routes)}\n')
f2.writelines([' '.join(map(str, route)) + '\n' for route in routes])
f2.close()