"""
Сравните два csv файла с данными о клиентских покупках за разные годы (2022 и 2023).
Определите, какие товары стали популярнее, а какие потеряли актуальность, сохраните
результат в новый csv файл.
"""
import csv
from collections import defaultdict

def compare_product_popularity(file_2022, file_2023, output_file5) :
    # Словари для хранения продаж товаров за каждый год
    sales_2022 = defaultdict(int)
    sales_2023 = defaultdict(int)

    # Внутренняя функция для извлечения данных
    def read_sales(file, sales_dict):
        with open(file, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # Пропускаем оглавление
            for row in reader:
                product, quantity = row[0], int(row[1])
                sales_dict[product] += quantity

    # Считываем данные из файлов
    read_sales("/Users/kamillasmidt/Python--2/Десятая лаба питон/2022.csv", sales_2022)
    read_sales("/Users/kamillasmidt/Python--2/Десятая лаба питон/2023.csv", sales_2023)

    # Сравниваем продажи и определяем изменения популярности
    results = []
    all_products = set(sales_2022.keys()).union(set(sales_2023.keys()))
    for product in all_products:
        sales_22 = sales_2022.get(product, 0)
        sales_23 = sales_2023.get(product, 0)
        change = sales_23 - sales_22
        results.append([product, sales_22, sales_23, change])

    # Передаем данные в файл output_file5.csv
    with open("/Users/kamillasmidt/Python--2/Десятая лаба питон/output_file5.csv", mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Product", "/Users/kamillasmidt/Python--2/Десятая лаба питон/2022.csv", "/Users/kamillasmidt/Python--2/Десятая лаба питон/2023.csv", "Change"])
        writer.writerows(results)

    print(f"Comparison results saved to '{"/Users/kamillasmidt/Python--2/Десятая лаба питон/output_file5.csv"}'.")
file_2022 = "/Users/kamillasmidt/Python--2/Десятая лаба питон/2022.csv"
file_2023 = "/Users/kamillasmidt/Python--2/Десятая лаба питон/2023.csv"
output_file5 = "/Users/kamillasmidt/Python--2/Десятая лаба питон/output_file5.csv"
c = compare_product_popularity(file_2022, file_2023, output_file5)
print(c)