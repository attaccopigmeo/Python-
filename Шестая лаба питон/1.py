# (a/b + c/d + k/m) * e/f
def GCD(n1, n2): # Определяем НОД чисел, алг. Евклида
    while n1 != 0 and n2 != 0: 
        if n1 > n2:
           n1 = n1 % n2
        else:
            n2 = n2 % n1
    return (n1 + n2)


def reduction_of_fractions(p, q): # Сокращение дроби
    n = GCD(p, q)
    p = p // n
    q = q // n
    return p, q


def sum_of_fractions(n1, n2, n3, n4):
    p = n1 * n4 + n2 * n3
    q = n2 * n4
    p, q = reduction_of_fractions(p, q)
    return p,q


def mult_of_fractions(n1, n2, n3, n4):
    p = n1 * n3
    q = n2 * n4
    p, q = reduction_of_fractions(p, q)
    return p,q


a, b, c, d, k, m, e, f = map(int, input().split())
p1, q1 = sum_of_fractions(a, b, c, d)
p2, q2 = sum_of_fractions(p1, q1, k, m)
p3, q3 = mult_of_fractions(p2, q2, e, f)
print(p3, q3)