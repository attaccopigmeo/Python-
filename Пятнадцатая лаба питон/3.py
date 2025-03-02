"""
На вход подаются сведения о клиентах фитнес-центра. В первой строке
указывается код K одного из клиентов, во второй строке — целое число N, а каждая из
последующих N строк имеет формат
<Год> <Номер месяца> <Код клиента> <Продолжительность занятий (в часах)>
Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента — в
диапазоне 10–99, продолжительность занятий — в диапазоне 1–30. Для каждого года, в котором
клиент с кодом K посещал центр, определить месяц, в котором продолжительность занятий
данного клиента была наименьшей для данного года (если таких месяцев несколько, то
выбирать месяц с наибольшим номером; месяцы с нулевой продолжительностью занятий не
учитывать). Сведения о каждом годе выводить на новой строке в следующем порядке: год,
номер месяца, продолжительность занятий в этом месяце. Упорядочивать сведения по
возрастанию номера года. Если данные о клиенте с кодом K отсутствуют, то вывести строку
«Нет данных».
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
entries = []

for _ in range(n):
    year = int(input("Введите год (2000-2010): "))
    month = int(input("Введите месяц (1-12): "))
    hours = int(input("Введите продолжительность занятий в часах (1-30): "))
    client_id = int(input("Введите код клиента (10-99): "))
    if 2000 <= year <= 2010 and 1 <= month <= 12 and 1 <= hours <= 30 and 10 <= client_id <= 99:
        entry = FitnessEntry(year, month, hours, client_id)
        entries.append(entry)

client_id = int(input("Введите код нужного клиента: "))
found_data = False
for year in range(2000, 2011):
    visits = [0] * 12
    for entry in entries:
        if entry.year != year:
            continue
        if entry.client_id != client_id:
            continue
        visits[entry.month - 1] += entry.hours #месяцы начинаются с 1
    
    min_visits = 720
    min_month = 0
    for month in range(0, 12):
        if visits[month] == 0:
            continue
        if visits[month] <= min_visits:
            min_visits = visits[month]
            min_month = month + 1
    
    if min_month != 0:
        print(f"В году {year} клиент {client_id} меньше всего занимался в месяц {month} - всего {min_visits} часов.")
        found_data = True

if not found_data:
    print("Нет данных.")