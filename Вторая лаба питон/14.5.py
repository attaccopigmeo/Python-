# Для натурального числа N, содержащего не более, чем 8 значащих цифр, выяснить,\
    # является ли его последовательность цифр при просмотре справа налево строго убывающей\
        # последовательностью.
N = int(input("Введите число N: "))
d1 = 10
d2 = 0
Result = True
while N > 0:
    d2 = N % 10
    if d2 >= d1:
        Result = False
        break
    d1 = d2
    N = N // 10
print(Result)
# Тесты
# input 1256789 output True
# input 1245 output True
# input 908751 output False