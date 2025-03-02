s = input("Введите слово: ")
rev_s = s[::-1]


def boyer_moore_horspool(text: str, pattern: str):
    m, n = len(pattern), len(text)
    #вариант, когда шаблон длиннее строки, не рассматриваем, в нашем случае это невозможно
    #таблица сдвигов
    shift_table = {char: m for char in set(text)}
    for i in range(m - 1):
        shift_table[pattern[i]] = m - 1 - i
    
    i = 0
    while i <= n - m:
        if text[i + m - 1] == pattern[-1]:  #быстрая проверка последнего символа
            if text[i:i + m] == pattern:  #полное сравнение шаблона
                return i
        i += shift_table.get(text[i + m - 1], m)  #сдвиг
    
    return -1  #если совпадений нет


result = boyer_moore_horspool(rev_s, s)
print(f"Слово '{s}' является палиндромом." if result != -1 else f"Слово '{s}' не палиндром.")
