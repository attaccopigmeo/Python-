# Составить программу разложения данного натурального числа на простые множители.\\
# Например, 200 = 2 ** 3 * 5 ** 2.
import math
    

def prime_factors(n): # Ищем простые множители
    i = 2 # Простые числа начинаются с 2
    factors = 0
    x = n
    while n > 1:
        if n % i == 0: # Проверяем делимость на i-е число
            factors = factors * (x + 1) + i # Записываем число в сист. счисл. с осн. x + 1, где каждая цифра - простой делитель
            n //= i
        else:
            i += 1   
    return factors


N = int(input("Введите число: "))
factors = prime_factors(N)
cur = 1
cnt = 1
while factors > 0:
    fact = factors % (N + 1)
    if cur == 1:
        cur = fact
    elif fact != cur:
        print(str(cur), str(cnt), sep = " ** ", end = " * ")
        cur = fact
        cnt = 1
    else:
        cnt += 1
    factors //= (N + 1)
print(str(cur), str(cnt), sep = " ** ")

# Тесты
# 15 = 3 * 5
# 200 = 2 ** * 5 ** 2
# 799 = 17 * 47