def is_bipartite(graph, n):
    # Цвета для вершин: 0 - не окрашено, 1 - первый поток, 2 - второй поток
    colors = [0] * n

    def dfs(vertex, color):
        colors[vertex] = color
        for neighbor in range(n):
            if graph[vertex][neighbor] == 1:  # Есть связь
                if colors[neighbor] == color:  # Конфликт цветов
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, 3 - color):
                    return False
        return True

    for v in range(n):
        if colors[v] == 0:  # Если вершина не посещена
            if not dfs(v, 1):  # Запускаем DFS с первым цветом
                return False, []
    
    # Разделяем студентов на два потока
    first_stream = [i + 1 for i in range(n) if colors[i] == 1]
    return True, first_stream


# Считывание данных из файла
filename = "/Users/kamillasmidt/Python--2/03_1.txt"  # Укажите нужный файл
with open(filename, "r") as file:
    n = int(file.readline().strip())  # Количество студентов
    graph = []
    for _ in range(n):
        graph.append(list(map(int, file.readline().strip().split())))

# Проверяем на двудольность
possible, first_stream = is_bipartite(graph, n)

# Вывод результата
if possible:
    print(*first_stream)  # Студенты первого потока
else:
    print("Невозможно")
# Ответ: 1 3 5 6 8 9 10 11 13 14 15 23 25