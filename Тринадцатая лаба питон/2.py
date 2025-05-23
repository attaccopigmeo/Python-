"""
Черепашка. На квадратной доске расставлены целые неотрицательные числа,
каждое из которых не превосходит 100. Черепашка, находящаяся в левом верхнем углу, мечтает
попасть в правый нижний. При этом она может переползать только в клетку справа или снизу и
хочет, чтобы сумма всех чисел, оказавшихся у нее на пути, была бы минимальной. Определить
эту сумму. Ввод и вывод организовать при помощи текстовых файлов. Формат входных данных:
в первой строке входного файла записано число N - размер доски (1<N<80). Далее следует N
строк, каждая из которых содержит N целых чисел, представляющих доску. В выходной файл
нужно вывести единственное число: минимальную сумму.
"""
f = open("/Users/kamillasmidt/Python--2/Тринадцатая лаба питон/2.txt", "r")
N = int(f.readline())
field = [[] for _ in range(N)]
for i in range(N):
    field[i] = list(map(int, f.readline().split()))
f.close()

# Таблица мемоизации
# i - коорд. по x, j - коорд. по y
# dp[i][j] - минимальная сумма чисел, которую можно собрать, дойдя до клетки (i, j)
dp = [[None for _ in range(N)] for _ in range(N)]
dp[0][0] = field[0][0] # в клетке (0, 0) мы безальтернативно соберём число из (0, 0)
# в крайние левые и верхние клетки путь один
for i in range(1, N): # краевые условия
    dp[i][0] = dp[i - 1][0] + field[i][0]
    dp[0][i] = dp[0][i - 1] + field[0][i]
for i in range(1, N):
    for j in range(1, N):
        # в остальные клетки можно прийти из клетки слева или клетки сверху
        # на основе этого можно определить минимальную сумму
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + field[i][j]
print("Минимальная сумма:", dp[N - 1][N - 1])