pattern = 'чечеткачечевица'
p = [0] * len(pattern)
j = 0
i = 1
while i < len(pattern):
    if pattern[i] == pattern[j]:
        j += 1
        p[i] = j
        i += 1
    else:
        if j != 0:
            j = p[j - 1]
        else:
            p[i] = 0
            i += 1

print(f"Префикс-функция строки-шаблона '{pattern}':", p)