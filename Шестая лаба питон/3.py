def check(num_str, p):
    for digit in num_str:
        # В системе счисл с осн p могут быть цифры только меньше p
        if int(digit) >= p:
            return False
    return True


def ten_in_p_f(dec_part, p):
    res = 0
    n = 0.1 # множитель для десятич. ф-мы
    cnt = 0
    while dec_part > 0 and cnt < 4:
        dec_part *= p
        digit = int(dec_part)
        res += digit * n
        n /= 10
        dec_part -= digit
        cnt += 1
    return res
# Переводим дробную часть из десятичной в p-ную

def ten_in_p(int_part, p):
    res = 0
    place = 1 #позиция в числе
    while int_part > 0:
        res += (int_part % p) * place
        place *= 10
        int_part //= p
    return res


def p_in_10(number, p):
    int_part = int(number)
    dec_part = number - int_part
    # Перевод цел. части
    res_int = 0
    place = 1
    while int_part > 0:
        res_int += (int_part % 10) * place
        int_part //= 10
        place *= p
    # Перевод дробной
    res_dec = 0.0
    n = p
    cnt = 0
    while dec_part > 0 and cnt < 4:
        dec_part *= 10
        digit = int(dec_part)
        res_dec += digit / n
        dec_part -= digit
        n *= p
        cnt += 1
    return res_int + res_dec


def calculate(x, y, z, p):
    x_10 = p_in_10(x, p)
    y_10 = p_in_10(y, p)
    z_10 = p_in_10(z, p)
    if z_10 == 0:
        return None
    res_10 = (x_10 + y_10) / z_10
    int_part = int(res_10)
    dec_part = res_10 - int_part
    res_int_p = ten_in_p(int_part, p)
    res_dec_p = ten_in_p_f(dec_part, p)
    return res_int_p + res_dec_p if res_dec_p else res_int_p


p = int(input("Введите осн. сист. счисл.: "))
x = int(input("Введите число x: "))
y = int(input("Введите число y: "))
z = int(input("Введите число z: "))
if check(str(int(x)), p) == False or check(str(int(y)), p) == False or check(str(int(z)), p) == False:
    print("Error")
else: 
    res = calculate(x, y, z, p)
    if res is not None:
        print(res)
    else:
        print("Error")