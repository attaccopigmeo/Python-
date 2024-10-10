# алгоритм перевода n в сист счисл с осн k
n = int(input())
k = int(input())
m = ""
while n > 0:
    m = str(n % k) + m
    n = n // k
print(m)