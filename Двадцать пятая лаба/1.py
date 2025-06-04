"""Имеется набор сообщений. Для данного сообщения написать программу с кодом Хемминга,
который позволит обнаруживать одиночную ошибку и исправлять ее. Привести решение
«вручную», в котором виден процесс построения кодов."""
"""00110000010010100"""


def hamming_code(data):
    """Вычисляет контрольные биты Хемминга для данных"""
    n = len(data)
    m = 0
    # Находим количество контрольных битов: 2^m >= m + n + 1
    while 2**m < m + n + 1:
        m += 1
    
    # Создаем закодированное сообщение с контрольными битами
    encoded = [0] * (n + m)
    j = 0
    # Заполняем биты данных (позиции, которые не являются степенями 2)
    for i in range(1, len(encoded) + 1):
        if (i & (i - 1)) != 0:  # Если i не степень 2...
        # Пояснение: степень 2 в двоичном виде выглядит как 10...0 (единица и далее нули),
        # при вычитании 1 получим 01...1 (единиц на 1 меньше, чем разрядов исходного числа)
        # и применение побитового И даст 0
        # в остальных случаях по крайней мере крайний левый бит останется равен 1, и побитовое И не даст 0
            # ...то переносим данные
            if j < n:
                encoded[i-1] = int(data[j])
                j += 1
    
    # Вычисляем контрольные биты
    for i in range(m):
        pos = 2**i - 1  # Позиция контрольного бита
        # Вычисляем XOR для всех битов, где (индекс+1) имеет установленный i-й бит
        xor = 0
        for j in range(pos, len(encoded), 2**(i+1)):
            for k in range(j, min(j + 2**i, len(encoded))):
                xor ^= encoded[k]
        encoded[pos] = xor
    
    return encoded

def hamming_correct(data):
    n = len(data)
    m = 0
    bits = []
    # Находим количество контрольных битов: 2^m >= m + n + 1
    while 2**m < m + n + 1:
        m += 1
        bits.append(m)

    # удаляем контрольные биты, чтобы произвести кодирование повторно
    data_to_recode = data
    bits.reverse()
    for bit in bits:
        data_to_recode = data_to_recode[:bit] + data_to_recode[(bit + 1):]
    encoding = hamming_code(data_to_recode)
    # позиция ошибочного бита определяется суммой номеров позиций контрольных битов
    # несовпадающих в исходном сообщении и закодированном вновь
    error_pos = 0
    for i in range(m):
        pos = 2 ** i - 1
        if data[pos] != encoding[pos]:
            error_pos += pos + 1
    if error_pos == 0:
        return None, data_to_recode
    error_pos -= 1
    # исправляем ошибочный бит
    data_corr = data[:error_pos] + ([1] if data[error_pos] == 0 else [0]) + data[(error_pos + 1):]
    # удаляем контрольные биты
    data_to_recode = data_corr
    bits.reverse()
    for bit in bits:
        data_to_recode = data_to_recode[:bit] + data_to_recode[(bit + 1):]
    return error_pos + 1, data_to_recode


data = list(map(int, input("Введите сообщение: ")))
error_pos, decoded = hamming_correct(data)
print('Позиция ошибки:', error_pos)
print('Декодированное сообщение: ', *decoded, sep='')
print('Код Хэмминга исходного сообщения: ', *hamming_code(decoded), sep='')