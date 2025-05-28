"""Дано описание неориентированного графа в текстовом файле с именем FileName1.
в виде матрицы смежности. Первая строка файла содержит количество вершин графа (n), а
следующие n строк содержат матрицу смежности (a), a[i][j]=0, если ребра между
вершинами i и j не существует. Построить матрицу инцидентности данного графа и
вывести ее в файл с именем FileName2. Для справки: матрица инцидентности (b) имеет
размер n x m, m - число ребер графа, b[i][j]=1, если ребро j инцидентно вершине i, в
противном случае b[i][j]=0. Нумерацию ребер осуществлять в следующем порядке:
сначала ребра, инцидентные вершине номер 1, потом ребра инцидентные вершине номер
2 и т.д. до вершины номер n. Ребра, инцидентные вершине с номером i перечислять в
порядке возрастания номера второй вершины, инцидентной данному ребру. При выводе в
первой строке указать размер матрицы инцидентности: числа n и m, а в следующих n
строках разместить матрицу инцидентности."""

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

filename = input('Введите FileName1: ')
# ВАЖНО! Если не будет находиться файл, нужно исправить строку 'Двадцать вторая лаба/'
#        Для этого нужно скопировать относительный путь файла, вставить его вместо строки,
#        после чего удалить название файла
f1 = open('Двадцать вторая лаба/' + filename, 'r')
adj_matrix = []
n = int(f1.readline())
for row in f1:
    adj_matrix.append(list(row.split()))
f1.close()

draw_adjacency_matrix(adj_matrix)

inc_matrix = [[] for _ in range(n)] # задаём n строк матрицы, изначально пустых
for i in range(n):
    # чтобы не смотреть одно и то же ребро дважды,
    # смотрим только те элементы матрицы, где j>i
    for j in range(i+1, n):
        if adj_matrix[i][j] != '0':
            # нашли ребро, тогда в матрице инцидентности в каждой строке добавляем значение:
            # 1 в строках i и j, 0 иначе
            for k in range(n):
                if k == i or k == j:
                    inc_matrix[k].append('1')
                else:
                    inc_matrix[k].append('0')

filename = input('Введите FileName2: ')
f2 = open('Двадцать вторая лаба/' + filename, 'w')
m = len(inc_matrix[0])
f2.write(f'{n} {m}\n')
f2.writelines([' '.join(inc_matrix[k]) + '\n' for k in range(n)])
f2.close()