def find(parent, i):
    # Функция для нахождения корня элемента i
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    # Функция для объединения двух поддеревьев
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(n, edges):
    # Алгоритм Крускала
    edges.sort(key=lambda x: x[2])  # Сортируем ребра по весу
    parent = list(range(n))
    rank = [0] * n
    mst = []
    total_weight = 0

    for edge in edges:
        u, v, weight = edge
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u != root_v:
            mst.append((u + 1, v + 1))  # Добавляем ребро (нумерация с 1)
            total_weight += weight
            union(parent, rank, root_u, root_v)

    return total_weight, mst


# Считывание данных из файла
filename = "/Users/kamillasmidt/Python--2/03_2.txt"  # Укажите файл с данными
with open(filename, "r") as file:
    n, m = map(int, file.readline().strip().split())
    edges = []
    for _ in range(m):
        x, y, l = map(int, file.readline().strip().split())
        edges.append((x - 1, y - 1, l))  # Приводим к нумерации с 0

# Нахождение минимального остовного дерева
total_weight, mst = kruskal(n, edges)

# Вывод результата
print(total_weight)
for edge in mst:
    print(edge[0], edge[1])
"""
Ответ:
10
4 5
6 7
7 8
2 3
5 6
1 2
3 4
8 9
"""