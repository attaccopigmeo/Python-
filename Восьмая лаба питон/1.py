# Создать словарь, в котором хранятся семь пар ключ-значение. Получите список всех ключей,//
# построчно распечатайте пары ключ-значение. Проверить – является ли введенное слово ключом.
# Дата заметки и ее содержание.
notes = {} #Cоздаем словарь

for _ in range(7): #Заполняем его
    date = input("Введите дату заметки: ")
    content = input("Введите содержание заметки: ")
    notes[date] = content

print("Список ключей: ", *notes.keys()) #Пара ключ-значение
for key in notes:
    print("Пара: ", key, notes[key])

n = int(input("Сколько раз вы бы хотели проверить даты? "))
for i in range(n): #Проверка дат
    date = input("Введите дату для проверки: ")
    if date in notes:
        print("Дата является ключом")
    else:
        print("Дата не является ключом")
"""
Введите дату заметки: 10.02.2003
Введите содержание заметки: qwerty
Введите дату заметки: 20.05.2015
Введите содержание заметки: kjhgfdds
Введите дату заметки: 29.04.2016
Введите содержание заметки: plkjn
Введите дату заметки: 13.12.2006
Введите содержание заметки: rfvbh
Введите дату заметки: 16.10.2020
Введите содержание заметки: rfdxuh
Введите дату заметки: 16.10.2020
Введите содержание заметки: yhgfdcv
Введите дату заметки: 22.07.2021
Введите содержание заметки: zxcvbnk
Список ключей:  10.02.2003 20.05.2015 29.04.2016 13.12.2006 16.10.2020 22.07.2021
Пара:  10.02.2003 qwerty
Пара:  20.05.2015 kjhgfdds
Пара:  29.04.2016 plkjn
Пара:  13.12.2006 rfvbh
Пара:  16.10.2020 yhgfdcv
Пара:  22.07.2021 zxcvbnk
Сколько раз вы бы хотели проверить даты? 2
Введите дату для проверки: 20.05.2015
Дата является ключом
Введите дату для проверки: 25.02.2006
Дата не является ключом
"""