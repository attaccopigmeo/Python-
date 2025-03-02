a = str(input()) #строка
b_in_a = str(input()) #подстрока
a_i = -1

for i in range(len(a) - len(b_in_a) + 1):
    for j in range(len(b_in_a)):
        if b_in_a[j] != a[i + j]:
            break
        else:
            a_i = i
            break

print(a_i)