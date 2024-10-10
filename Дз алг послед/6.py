def NOD(a, b): 
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def ADD(a, b, c, d):
    p = a * d + b * c
    q = b * d
    n = NOD(p, q) #сокращаем дробь
    p = p // n
    q = q // n
    return p, q


n = int(input("Введите кол-во слагаемых: "))
p = 0
q = 1
for i in range(1, n + 1):
    p, q = ADD(p, q, 1, i)
print("Дробь: ", p, "/", q)