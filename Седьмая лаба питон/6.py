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


def is_symmetric(M, matrix):
    for i in range(M):
        for j in range(i + 1, N):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def print_matrix(a): # Выводим матрицу
    for row in a:
        print(*row)


matrix = []
M = int(input("Введите кол-во строк матрицы: "))
N = M # Симметрия может быть только у квадратных матриц
print("Введите матрицу: ")
for _ in range(M):
    matrix.append(list(map(int, input().split())))
matrix_transpose = transpose(matrix)
print("Транспонированная матрица:")
print_matrix(matrix_transpose)
if is_symmetric(M, matrix):
    print("Матрица симметрична")
else:
    print("Матрица не симметрична")
# Tests
# Введите матрицу: 
# 1 1 1
# 1 1 1
# 1 1 1
# Транспонированная матрица:
# 1 1 1
# 1 1 1
# 1 1 1
# Введите кол-во строк матрицы: 4
# Введите матрицу: 
# 1 4 5 6
# 7 9 0 1
# 4 5 77 9
# 22 4 6 1
# Транспонированная матрица:
# 1 7 4 22
# 4 9 5 4
# 5 0 77 6
# 6 1 9 1
# Матрица не симметрична
# Введите кол-во строк матрицы: 3
# Введите матрицу: 
# 2 3 -1
# 3 5 -4
# -1 -4 7
# Транспонированная матрица:
# 2 3 -1
# 3 5 -4
# -1 -4 7
# Матрица симметрична