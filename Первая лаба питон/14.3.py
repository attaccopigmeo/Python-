#Вариант 14
x = int(input("Введите первый операнд: "))
y = int(input("Теперь второй: "))
z = 0
v = 0
operation = int(input("Определимся с побитовой операцией. Введите цифру от 1 до 5: "))
match operation:
    case 1:
        z = x & y
    case 2:
        z = x | y
    case 3:
        z = x ^ y
    case 4:
        z = x << 1
        v = y << 1
    case 5:
        z = x >> 1
        v = y >> 1
print("Результат операции: ", z, v)