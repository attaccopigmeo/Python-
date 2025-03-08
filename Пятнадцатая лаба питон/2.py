"""
Имеется информация об учениках младшей школы. Для всех учеников известны:
фамилия, имя и класс. Для учеников 1-х классов дополнительно известна их скорость чтения
(слов в минуту, тип int). Для учеников 4-х классов известны баллы итоговой аттестации (единый
муниципальный тест от 1 до 100 баллов, тип float). Для учеников 2-х и 3-х классов известны
данные итоговой школьной контрольной по математике (оценки от 1 до 10 баллов, тип float).
Написать функцию, позволяющую ввести с клавиатуры данные для одного ученика. Используя
эту функцию, ввести сведения об N учениках и сохранить их в бинарном файле. Распечатать на
экране содержимое данного файла в виде таблицы.
"""
# Наследственность, подклассы

import pickle
import pandas as pd
#Основной класс
class Student:
    def __init__(self, last_name, first_name, grade):
        self.last_name = last_name
        self.first_name = first_name
        self.grade = grade

    def __repr__(self):
        return f'{self.last_name} {self.first_name}, {self.grade} класс'

#Подклассы
class FirstGradeStudent(Student):
    def __init__(self, last_name, first_name, read_speed):
        super().__init__(last_name, first_name, 1)
        self.read_speed = read_speed
    
    def __repr__(self):
        return super().__repr__() + f': скорость чтения {self.read_speed} слов в минуту'
    

class SecondGradeStudent(Student):
    def __init__(self, last_name, first_name, math_exam):
        super().__init__(last_name, first_name, 2)
        self.math_exam = math_exam

    def __repr__(self):
        return super().__repr__() + f': итоговая контрольная по математике {self.math_exam} баллов'
    

class ThirdGradeStudent(Student):
    def __init__(self, last_name, first_name, math_exam):
        super().__init__(last_name, first_name, 3)
        self.math_exam = math_exam

    def __repr__(self):
        return super().__repr__() + f': итоговая контрольная по математике {self.math_exam} баллов'
    

class FourthGradeStudent(Student):
    def __init__(self, last_name, first_name, final_exam):
        super().__init__(last_name, first_name, 4)
        self.final_exam = final_exam

    def __repr__(self):
        return super().__repr__() + f': итоговая аттестация {self.final_exam} баллов'

def input_student():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    grade = int(input("Введите класс (1-4): "))
    student = None

    if grade == 1:
        read_speed = int(input("Введите скорость чтения (слов в минуту): "))
        student = FirstGradeStudent(last_name, first_name, read_speed)
    elif grade == 4:
        final_exam = float(input("Введите результат муниципального теста (1-100): "))
        student = FourthGradeStudent(last_name, first_name, final_exam)
    else:
        math_exam = float(input("Введите оценку за итоговую контрольную по математике (1-10): "))
        if grade == 2:
            student = SecondGradeStudent(last_name, first_name, math_exam)
        else:
            student = ThirdGradeStudent(last_name, first_name, math_exam)
    
    return student

filename = "students.dat"
n = int(input("Введите кол-во студентов: "))

students = [input_student() for _ in range(n)]

with open(filename, "wb") as file:
    pickle.dump(students, file)

with open(filename, "rb") as file:
    loaded_students = pickle.load(file)

data = [{"Фамилия": s.last_name, "Имя": s.first_name, "Результаты": s.read_speed} for s in loaded_students if s.grade == 1]
df = pd.DataFrame(data)

if len(data) != 0:
    print("\nРезультаты учеников 1-го класса:")
    print(df)

data = [{"Фамилия": s.last_name, "Имя": s.first_name, "Класс": s.grade, "Результаты": s.math_exam} for s in loaded_students if s.grade == 2]
df = pd.DataFrame(data)

if len(data) != 0:
    print("\nРезультаты учеников 2-го класса:")
    print(df)

data = [{"Фамилия": s.last_name, "Имя": s.first_name, "Класс": s.grade, "Результаты": s.math_exam} for s in loaded_students if s.grade == 3]
df = pd.DataFrame(data)

if len(data) != 0:
    print("\nРезультаты учеников 3-го класса:")
    print(df)

data = [{"Фамилия": s.last_name, "Имя": s.first_name, "Класс": s.grade, "Результаты": s.final_exam} for s in loaded_students if s.grade == 4]
df = pd.DataFrame(data)

if len(data) != 0:
    print("\nРезультаты учеников 4-го класса:")
    print(df)
