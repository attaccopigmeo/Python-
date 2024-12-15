"""
Построить диаграмму рассеяния для отношения удельной стоимости к удельному
объему отходов. Добавить заголовок, легенду и подписи к осям. Данные находятся в файле
3.xlsx строки с 91 по 120.
"""
from pylab import *
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel("/Users/kamillasmidt/Python--2/Одиннадцатая лаба питон/3.xlsx", usecols="J,K").iloc[90:118]
plt.scatter(data["Удельная стоимость на 1 га в ценах 2023 г, тыс. руб."], data["Удельный объем отходов на 1 га, тонн"], label = "Полигоны")
plt.title("Отношение уд. стоимости к уд. объему")
plt.xlabel("Удельная стоимость")
plt.ylabel("Удельный объем")
plt.legend()
plt.tight_layout() # Подстраивает размеры объектов
plt.grid(True)
plt.show()