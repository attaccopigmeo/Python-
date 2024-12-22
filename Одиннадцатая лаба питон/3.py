"""
Построить столбчатую диаграмму по химическому составу отходов. Добавить
заголовок, легенду и подписи к осям. Данные находятся в файле 2.xlsx, вариант указан в
первом столбце.
"""
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd

# Выбираем столбцы и строки с которых считываем данные
data = pd.read_excel("/Users/kamillasmidt/Python--2/Одиннадцатая лаба питон/2.xlsx", usecols="E,G", header = 1).iloc[290:310]
# Стобчатая диаграмма
plt.bar(data["Вещество"], data["значение"], label = "Содержание отходов")
plt.xticks(rotation = 90) # Меняет угол надписей
plt.title("Хим. состав отходов")
plt.xlabel("Вещество")
plt.ylabel("Содержание")
plt.legend()
plt.tight_layout() # Подстраивает размеры объектов
plt.show()