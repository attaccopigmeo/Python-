"""
pyplot
Построить график функции y=-x2-7x+2 
для x в диапазоне от -10 до 10. Добавьте
заголовок и легенду, график должен быть синего цвета.
"""
from pylab import *
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 1000) # Равномерно расставляем n чисел в диапазоне [a, b]
y = - x ** 2 - 7 * x + 2
plt.plot(x, y, color = "b") # Отрисовка графика
plt.show()