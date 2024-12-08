"""
Дан файл формата csv с данными о продажах компьютерной техники: фамилия, месяц,
товар и сумма. Вывести на экран строки с минимальными продажами за каждый месяц.
"""
import pandas as pd

df = pd.read_csv("/Users/kamillasmidt/Python--2/Десятая лаба питон/1.csv")
print("Минимальные продажи за месяц")
print(df.groupby("month", as_index=False).min()[["month","sum"]])
"""
Минимальные продажи за месяц
       month    sum
0     Август  12000
1     Апрель  12000
2    Декабрь  45000
3       Июль  40000
4       Июнь  55000
5        Май  60000
6       Март   8000
7     Ноябрь   7000
8    Октябрь  18000
9   Сентябрь  95000
10   Февраль  10000
11    Январь  20000
"""