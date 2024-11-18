# Сколько существует пятизначных чисел, у которых сумма цифр четна?
count = 0
for i in range(10000, 100000):
    n = i
    Sum = 0
    while n > 0:
        Sum += n % 10
        n //= 10
    if Sum % 2 == 0:
        count +=1
print("Amount of five-digit numbers whose sum of digits is an even number:", count)