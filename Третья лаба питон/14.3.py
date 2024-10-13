# Найдите все числа Фибоначчи с номерами от N1 до N2. Ответ записать в файл c\
    # именем b.txt, располагая по одному числу в строке. Рекуррентное соотношение для чисел\
        # Фибоначчи: F0 = 0, F1 = 1, Fi = Fi-1+Fi-2 при i>1.
def Fibonacci(F):
    if F == 1 or F == 2:
        return(1)
    elif F > 2:
        F = Fibonacci(F - 1) + Fibonacci(F - 2)
        return(F)
    elif F == 0:
        return(0)
    else:
        return("")



N1 = int(input("Введите нижнюю границу: "))
N2 = int(input("Введите верхнюю границу: "))
F = "0"
f = open("./b1.txt", "w")
for i in range(N1, N2, 1):
    F = str(Fibonacci(i))
    f.write(F + "\n")
f.close()