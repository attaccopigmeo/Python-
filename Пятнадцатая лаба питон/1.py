"""
На вход подаются сведения о клиентах фитнес-центра. В первой строке
указывается целое число N, а каждая из последующих N строк имеет формат
<Год> <Номер месяца> <Продолжительность занятий (в часах)> <Код клиента>
Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента — в
диапазоне 10–99, продолжительность занятий — в диапазоне 1–30. Найти строку исходных
данных с максимальной продолжительностью занятий. Вывести эту продолжительность, а
также соответствующие ей год и номер месяца (в указанном порядке). Если имеется несколько
строк с максимальной продолжительностью, то вывести данные той из них, которая является
первой в исходном наборе.
"""

class FitnessEntry:
    def __init__(self, year, month, hours, client_id):
        self.year = year
        self.month = month
        self.hours = hours
        self.client_id = client_id

    def __repr__(self):
        return f"{self.hours} {self.year} {self.month}"

n = int(input("Введите кол-во клиентов, которых хотите записать: "))
max_entry = None

for _ in range(n):
    year = int(input("Введите год (2000-2010): "))
    month = int(input("Введите месяц (1-12): "))
    hours = int(input("Введите продолжительность занятий в часах (1-30): "))
    client_id = int(input("Введите код клиента (10-99): "))
    if 2000 <= year <= 2010 and 1 <= month <= 12 and 1 <= hours <= 30 and 10 <= client_id <= 99:
        entry = FitnessEntry(year, month, hours, client_id)
        if max_entry is None or entry.hours > max_entry.hours:
            max_entry = entry

if max_entry:
    print(max_entry)

