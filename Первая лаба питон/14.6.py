print("Вычисление площади круга по длине окружности: ")
П = 3.1415
L = float(input("Введите длину окружности (см) -> "))
S = 0.25 * (L**2 / П)
print("Площадь круга %.2f кв. см" % S)
#input >> 23
#output << 42.10 кв. см.
#input >> 62.83
#output << 314.15
#input >> 4
#output << 1.27