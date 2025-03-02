"""
Даны три файла вещественных чисел с именами S1, S2 и S3, элементы которых
упорядочены по убыванию. Объединить эти файлы в новый файл с именем S4 так, чтобы его
элементы также оказались упорядоченными по убыванию.
"""
import struct
import random


def create_bin_file(n, filename):
    with open(filename, 'wb') as file:
        for i in range(n):
            x = random.random() #генерируем случайное (от 0 до 1) вещественное число
            file.write(struct.pack('f', x))
            print(x)

def read_array(filename):
    with (open(filename, 'rb') as file):
        packed_data = file.read()
        N = len(packed_data) // 4   #можно определить количество байтов в списке (каждое число 4 байта) 
        return struct.unpack('f' * N, packed_data)


S1_file, S2_file, S3_file = input("Введите названия файлов (в конце .bin, через пробел): ").split()
n1, n2, n3 = int(input("Введите кол-во элементов в каждом из файлов (через пробел): ")).split()
create_bin_file(n1, S1_file)
create_bin_file(n2, S2_file)
create_bin_file(n3, S3_file)
S1 = read_array(S1_file)
S2 = read_array(S2_file)
S3 = read_array(S3_file)
i1, i2, i3 = 0, 0, 0
S = []
while (i1 < len(S1)) or (i2 < len(S2)) or (i3 < len(S3)):
    if (i1 < len(S1)) and (S1[i1] >= S2[i2]) and (S1[i1] >= S3[i3]):
        S.append(S1[i1])
        i1 += 1