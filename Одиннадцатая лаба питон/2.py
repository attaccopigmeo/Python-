"""
Построить гистограмму. Добавить заголовок, легенду и подписи к осям. Данные
находятся в файле 1.xlsx, строки с 51 по 100.
"""
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel("/Users/kamillasmidt/Python--2/Одиннадцатая лаба питон/1.xlsx", sheet_name="первый вариант методики", index_col=0)
# index_col=0 - первый столбик - это столбик с номерами
data = data.iloc[50:100] #отбираем строки в диапазоне
plt.figure().set_facecolor("#D2CBB9")
ax = plt.axes()
ax.set_facecolor("#DCD6C3")
plt.hist(data["Количество отходов переданных на захоронение"], label = "Кол-во отходов на захоронение")
plt.title("Захоронение отходов")
plt.xlabel("Кол-во отходов")
plt.ylabel("Субъекты")
plt.legend()
plt.show()