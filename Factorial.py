def Factorial(n, s):
    if n >= 1:
        s = s * n
        return Factorial(n - 1, s)
    return s
n = int(input("Введите число: "))
print(Factorial(n, 1))