# Вариант 29
# №1
def create_set(L):
    a = 0
    for x in L:
        a += 1 << x
    return a


def restore(a):
    L = []
    n = 0
    while a != 0:
        has = a % 2
        if has == 1:
            L.append(n)
        a //= 2
        n += 1
    return L


A = [1, 2, 5, 9, 14, 17, 19, 23, 25, 26, 27, 28, 30, 34, 35, 39, 41, 42, 43, 44, 45, 49, 50]
B = [3, 4, 6, 7, 10, 13, 15, 20, 22, 24, 25, 26, 27, 29, 30, 34, 35, 36, 38, 39, 41, 44, 48, 49]
C = [4, 5, 14, 17, 18, 19, 20, 21, 23, 29, 30, 31, 33, 34, 35, 36, 38, 42, 44, 45]
D = [2, 5, 6, 7, 9, 10, 11, 13, 14, 16, 17, 20, 21, 22, 23, 25, 28, 29, 31, 32, 33, 34, 36, 37, 40, 42, 43, 44, 45, 47, 49]
a = create_set(A)
b = create_set(B)
c = create_set(C)
d = create_set(D)

res1 = ((a & b) | a) ^ ((((c & a) & (~(b ^ a))) & ((b ^ c) & (~((c | b) ^ a)))) | ((c & (~d)) & (a & d)))
res2 = (((d ^ c) | a) & ((d & b) & d)) ^ (((c & d) & ((a ^ b) ^ a)) | ((d & b) & ((d | a) & d)))
res3 = (((a & (~d)) & ((d & (~c)) & ((a & (~b)) ^ a))) & ((b & c) & (d | b))) & (~((c & (~a)) & (~((b & d) ^ b))))

print(restore(res1))
print(restore(res2))
print(restore(res3))
# ___________________________
# №2
# (7 - 7 * x + 4 * x ** 3 - 3 * x ** 6) ** 10
def factorial(n, s = 1):
    if n >= 1:
        s = s * n
        return factorial(n - 1, s)
    return s


def multinomial(a, b, c, d):
    return factorial(a + b + c + d) // (factorial(a) * factorial(b) * factorial(c) * factorial(d))


for i in range(0, 61, 1):
    s = 0 # Коэффициент
    for k in range(0, 11, 1):
        for m in range(0, 11 - k, 1):
            for n in range(0, 11 - k - m, 1):
                l = 10 - k - m - n
                if l < 0:
                    continue
                if k + 3 * m + 6 * n != i:
                    continue
                s += multinomial(k, l, n, m) * 7 ** l * (-7) ** k * 4 ** m * (-3) ** n
    print(s)