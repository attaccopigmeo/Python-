"""
Дан файл целых чисел, содержащий более 50 элементов. Уменьшить его размер до 50
элементов, удалив из файла необходимое количество конечных элементов.
"""
import struct
import random

def create_bin_file(n, filename):
    with open(filename, 'wb') as file:
        for i in range(n + 50):
            x = random.randint(-100, 100) #генерируем случайное (от 0 до 1) вещественное число 
            file.write(struct.pack('i', x))
            print(x)


def rm_excess(filename):
    unpacked_data = None
    with (open(filename, 'rb') as file):
        packed_data = file.read()
        N = len(packed_data) // 4   #можно определить количество байтов в списке (каждое число 4 байта) 
        unpacked_data = struct.unpack('i' * N, packed_data)
    with open(filename, 'wb') as file:
        print("Оставшиеся числа:")
        for x in unpacked_data[:50]:
            file.write(struct.pack('i', x))
            print(x)


filename = input("Введите название файла (в конце .bin): ")
n = int(input("Введите кол-во лишних элементов: "))
create_bin_file(n, filename)
rm_excess(filename)

"""
Введите название файла (в конце .bin): 3.bin
Введите кол-во лишних элементов: 5
-22
68
-63
19
-43
60
19
16
56
72
47
-72
-69
48
22
-16
-48
-52
-57
-2
45
-64
26
72
49
-47
-85
32
99
-39
-10
5
11
83
-29
28
-31
-18
46
56
43
-23
25
96
98
69
-40
67
90
22
-86
-42
-31
-88
19
Оставшиеся числа:
-22
68
-63
19
-43
60
19
16
56
72
47
-72
-69
48
22
-16
-48
-52
-57
-2
45
-64
26
72
49
-47
-85
32
99
-39
-10
5
11
83
-29
28
-31
-18
46
56
43
-23
25
96
98
69
-40
67
90
22
"""