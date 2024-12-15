"""
Дан файл формата csv с данными о заказах: название компании, название товара, объем.
Товары доставляются на двух видах транспорта: газель объемом до 10 м3 и фура объемом до
80 м3. Вывести на экран все кампании и заказы которым для доставки достаточно отправить
газель.
"""
import csv

def find_orders_for_gazel(file_path):
    print("Компания", "Товар", sep = "\t")
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader: # Обрабатываем каждую строку
            if int(row["volume"]) <= 10:
                print(row["nameofcompany"], row["nameofgood"], sep = "\t")


file_path = "/Users/kamillasmidt/Python--2/Десятая лаба питон/2.csv"
find_orders_for_gazel(file_path)

"""
Компания        Товар
Рога и копыта   рога
Мин. правды     газеты
А Ежи           иглы
Мир любви       смута
Вселенная игр   покер
Мир любви       грабли
Супный мир      кастрюли
"""