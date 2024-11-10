def generate_two_numbers():
    global seed

    # Параметры для линейного конгруэнтного генератора
    a = 1103515245
    c = 12345
    m = 2**31

    
    # Генерируем первое число
    seed = (a * seed + c) % m
    num1 = seed % 9 + 2

    # Генерируем второе число на основе обновленного seed
    seed = (a * seed + c) % m
    num2 = seed % 9 + 2

    return num1, num2


def question(a, b):
    c = int(input(str(a) + " * " + str(b) + " = "))
    return c


def proverka(a, b, c):
    return a * b == c


def ball(res, score):
    if res:
        score += 1
    return score


def mark(score, total):
    if score >= total * 0.8:
        return 5
    elif score >= total * 0.6:
        return 4
    elif score >= total * 0.4:
        return 3
    else:
        return 2
    
seed = 123456789 # Инициализируем начальное значение (seed)
n = int(input("Введите кол-во вопросов: "))
score = 0
for i in range(n):
    a, b = generate_two_numbers()
    c = question(a, b)
    score = ball(proverka(a, b, c), score)
print("Ваша оценка:", mark(score, n))