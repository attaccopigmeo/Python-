"""
Создайте три файла формата csv с данными о студентах (не менее 5 записей, не менее 3
параметров). Объедините эти файлы в один удалив дубликаты записей.
"""
import csv

# Ф-ция передачи инфо из трех файлов в другой
def merge_csv_files(input_file1, input_file2, input_file3, output_file):
    input_files = [input_file1, input_file2, input_file3]

    try:
        # Создаем и открываем output_file для записи
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = None

            for file in input_files:
                with open(file, mode='r', encoding='utf-8') as infile:
                    reader = csv.reader(infile)
                    writer.writerows(reader) # Записываем строки в созданный файл

        print(f"Данные из {len(input_files)} файлов успешно переданы в '{output_file}'. Можете проверить!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


for i in range(5):
    name = input("Введите имя студента: ")
    surname = input("Введите фамилию студента: ")
    average_score = input ("Введите средний балл студента: ")
    f = open("/Users/kamillasmidt/Python--2/Десятая лаба питон/students1.csv","a")
    f.write(f"{name},{surname},{average_score}\n")

for i in range(5):
    name = input("Введите имя студента: ")
    surname = input("Введите фамилию студента: ")
    average_score = input ("Введите средний балл студента: ")
    f = open("/Users/kamillasmidt/Python--2/Десятая лаба питон/students2.csv","a")
    f.write(f"{name},{surname},{average_score}\n")

for i in range(5):
    name = input("Введите имя студента: ")
    surname = input("Введите фамилию студента: ")
    average_score = input ("Введите средний балл студента: ")
    f = open("/Users/kamillasmidt/Python--2/Десятая лаба питон/students3.csv","a")
    f.write(f"{name},{surname},{average_score}\n")

c = merge_csv_files("/Users/kamillasmidt/Python--2/Десятая лаба питон/students1.csv", "/Users/kamillasmidt/Python--2/Десятая лаба питон/students2.csv", "/Users/kamillasmidt/Python--2/Десятая лаба питон/students3.csv", "/Users/kamillasmidt/Python--2/Десятая лаба питон/output_file.csv")
print(c)