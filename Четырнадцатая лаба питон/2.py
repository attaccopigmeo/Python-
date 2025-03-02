"""
Дан файл вещественных чисел. Найти его первый локальный минимум (локальным
минимумом называется элемент, который меньше своих соседей).
"""

import struct
import random


def create_bin_file(n, filename):
    with open(filename, 'wb') as file:
        for i in range(n):
            x = random.random() #генерируем случайное (от 0 до 1) вещественное число
            file.write(struct.pack('f', x))
            print(x)


def find_local_min(filename):
    with (open(filename, 'rb') as file):
        packed_data = file.read()
        N = len(packed_data) // 4   #можно определить количество байтов в списке (каждое число 4 байта) 
        unpacked_data = struct.unpack('f' * N, packed_data)
        for i in range(len(unpacked_data)):
            if (i == 0 or unpacked_data[i] < unpacked_data[i - 1]) and \
                (i == len(unpacked_data) - 1 or unpacked_data[i] < unpacked_data[i + 1]):
                print("Локальный минимум:", unpacked_data[i])
                break


filename = input("Введите название файла (в конце .bin): ")
n = int(input("Введите кол-во элементов: "))
create_bin_file(n, filename)
find_local_min(filename)

"""
Введите название файла (в конце .bin): 3.bin
Введите кол-во элементов: 9
0.5364169995328241
0.5752576747544449
0.8423626905648989
0.7504045432079005
0.019120192441119177
0.28533819165755436
0.1296363259558282
0.022988774956754887
0.9686742904672477
Локальный минимум: 0.5364170074462891
"""
