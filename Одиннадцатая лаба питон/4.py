"""
Построить секторную диаграмму по морфологическому составу отходов. Добавить
заголовок, легенду. Данные находятся в файле 2.xlsx, вариант указан в первом столбце.
"""
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel("/Users/kamillasmidt/Python--2/Одиннадцатая лаба питон/2.xlsx", usecols="H,J", header = 1).iloc[289:299]
print(data)
plt.pie(data["значение.1"], labels = data["Компонент"])
plt.title("Морф. состав отходов")
plt.tight_layout() # Подстраивает размеры объектов
plt.show()