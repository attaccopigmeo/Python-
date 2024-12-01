# Поменять максимальный элемент матрицы B размерности N x M с его первым//
# элементом, а минимальный - с последним. В матрице только один максимальный и один//
# минимальный элемент
def input_matrix(): # Функция для ввода матрицы пользователем
    M, N = map(int, input("Введите количество строк и столбцов матрицы (через пробел): ").split())
    matrix = []
    print("Введите элементы матрицы построчно (через пробел):")
    for i in range(N):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        while len(row) != M:
            print(f"Ошибка: в строке должно быть {M} элементов. Попробуйте ещё раз.")
            row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    return matrix


# Функция для замены максимального элемента с первым, минимального с последним
def swap_matrix_elements(matrix):
    M = len(matrix)
    N = len(matrix[0])
    # Инициализация значений и индексов для максимального и минимального элементов
    max_value = matrix[0][0]
    max_pos = (0, 0)
    min_value = matrix[0][0]
    min_pos = (0, 0)
    for i in range(M): # Поиск максимального и минимального элемента
        for j in range(N):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_pos = (i, j)
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_pos = (i, j)
    # Обмен максимального элемента с первым элементом
    matrix[max_pos[0]][max_pos[1]], matrix[0][0] = matrix[0][0], matrix[max_pos[0]][max_pos[1]]
    if min_pos == (0, 0):
        min_pos = max_pos
    # Обмен минимального элемента с последним элементом
    matrix[min_pos[0]][min_pos[1]], matrix[M-1][N-1] = matrix[M-1][N-1], matrix[min_pos[0]][min_pos[1]]
    return matrix


matrix = input_matrix()
print("\nИсходная матрица:")
for row in matrix:
    print(*row)
matrix = swap_matrix_elements(matrix)
print("\nМатрица после замены:")
for row in matrix:
    print(*row)
# Тесты
# Введите количество строк и столбцов матрицы (через пробел): 3 3
# Введите элементы матрицы построчно (через пробел):
# Строка 1: 1 2 3
# Строка 2: 3 4 6
# Строка 3: 7 9 5
# 
# Исходная матрица:
# 1 2 3
# 3 4 6
# 7 9 5
# 
# Матрица после замены:
# 9 2 3
# 3 4 6
# 7 5 1
# Введите количество строк и столбцов матрицы (через пробел): 3 3
# Введите элементы матрицы построчно (через пробел):
# Строка 1: 3 4 5
# Строка 2: 3 7 1
# Строка 3: 8 6 88
# 
# Исходная матрица:
# 3 4 5
# 3 7 1
# 8 6 88
# 
# Матрица после замены:
# 88 4 5
# 3 7 3
# 8 6 1