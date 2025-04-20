"""
Реализовать в виде рекурсивной процедуры или функции, itertools не использовать.
Необходимо записывать путь: Вверх, Вправо, Вниз, Влево. Если мышка идет обратно - убираем последний шаг.
Задача поиска сыра в лабиринте. Дан лабиринт размером NхN (N<=15). Форма
лабиринта записана в текстовом файле, стена обозначается символом М, отсутствие стены -
символом пробела. Даны координаты мышки в лабиринте (номер строки (X) и номер столбца
(Y)) и координаты сыра (номер строки (XС) и номер столбца (YС)). Нужно посчитать
количество возможных различных путей мышки к сыру.
"""

def count_paths(maze, x, y, cheese_x, cheese_y, visited):
    # Проверка выхода за границы и на стену
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze):
        return 0
    if maze[x][y] == 'M' or visited[x][y]:
        return 0
    # Найден путь к сыру
    if x == cheese_x and y == cheese_y:
        return 1

    visited[x][y] = True  # Помечаем текущую клетку как посещённую

    # Переходы: вверх, вниз, влево, вправо
    total_paths = (
        count_paths(maze, x - 1, y, cheese_x, cheese_y, visited) +
        count_paths(maze, x + 1, y, cheese_x, cheese_y, visited) +
        count_paths(maze, x, y - 1, cheese_x, cheese_y, visited) +
        count_paths(maze, x, y + 1, cheese_x, cheese_y, visited)
    )

    visited[x][y] = False  # Возврат: снять метку посещения

    return total_paths


def read_maze_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        maze = [list(line.rstrip('\n')) for line in f]
    return maze


def find_all_paths(filename, mouse_x, mouse_y, cheese_x, cheese_y):
    maze = read_maze_from_file(filename)
    visited = [[False] * len(maze) for _ in range(len(maze))]
    return count_paths(maze, mouse_x, mouse_y, cheese_x, cheese_y, visited)


if __name__ == '__main__':
    filename = 'Двадцатая лаба/maze.txt'
    mouse_x, mouse_y = map(int, input("Введите координаты мыши: ").split())
    cheese_x, cheese_y = map(int, input("Введите координаты сыра: ").split())
    paths = find_all_paths(filename, mouse_x, mouse_y, cheese_x, cheese_y)
    print(f'Количество путей: {paths}')
