def count_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // 1)
    return len(divisors)


number = input("Enter your number: ")
while not number.isdigit() or int(number) <= 0:
    print("Enter positive number!!!")
    number = input("Enter the number again: ")
result = count_divisors(int(number))
print("Total amount of divisors of the number: ", result)