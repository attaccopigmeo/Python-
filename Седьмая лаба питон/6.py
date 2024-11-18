# Задана квадратная матрица. Получить транспонированную матрицу и проверить,//
# является ли исходная матрица симметричной относительно главной диагонали
def transpose(matrix): # Транспонирование матрицы
    matrix_transpose = []
    for i in range(len(matrix)): # Заполняем новуб матр. нулями (делаем заготовку)
        matrix_transpose.append([0] * len(matrix)) 
    for i in range(len(matrix)): # Заполняем нужными эл. заготовку
        for j in range(len(matrix)):
            matrix_transpose[i][j] = matrix[j][i]
    return matrix_transpose


def is_equal(mat1, mat2): # Сравниваем исходную матр. с транспонированной, т.к. матр. симметрична, если = транспонированной
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            if mat1[i][j] != mat2[i][j]:
                return False
    return True


def print_matrix(a): # Выводим матрицу
    for row in a:
        print(*row)


matrix = []
M, N = map(int, input("Введите размер матрицы (кол-во строк, кол-во столбцов (через пробел)): ").split())
print("Введите матрицу: ")
for _ in range(M):
    matrix.append(list(map(int, input().split())))
matrix_transpose = transpose(matrix)
print("Транспонированная матрица:")
print_matrix(matrix_transpose)
if is_equal(matrix, matrix_transpose):
    print("Матрицы симметричные")
else:
    print("Матрицы не симметричные")
# Tests
# Введите матрицу: 
# 1 2 3
# 4 5 6
# 7 8 9
# Транспонированная матрица:
# 1 4 7
# 2 5 8
# 3 6 9
# Матрицы не симметричные
# Введите матрицу: 
# 2 3 -1
# 3 5 -4
# -1 -4 7
# Транспонированная матрица:
# 2 3 -1
# 3 5 -4
# -1 -4 7
# Матрицы симметричные
# Введите матрицу: 
# 1 2 3 4
# 5 7 9 0
# 3 44 5 5  
# 1 4 2 5
# Транспонированная матрица:
# 1 5 3 1
# 2 7 44 4
# 3 9 5 2
# 4 0 5 5
# Матрицы не симметричные