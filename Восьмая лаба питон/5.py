# Имеются сведения о программах телепередач на неделю: день недели, время, канал, вид
# и название телепередачи.
# а) Получить название телепередач, которые идут в указанный день в указанный промежуток
# времени.
# б) Выяснить, есть ли передача, транслирующаяся больше одного раза в одно и то же время. Если
# есть, то какая?
# в) Получить информацию об указанном фильме. Если он отсутствует в телепрограмме, то
# вывести на экран сообщение «такой передачи на данной неделе нет»
def read_schedule_from_file(file_path): #Функция преобразования данных в словари
    schedule = []
    with open(file_path, "r") as file:
        for line in file:
            day, time, channel, type_, name = line.strip().split(",")
            schedule.append({
                "день": day,
                "время": time,
                "канал": channel,
                "тип": type_,
                "наименование": name
            })
    return schedule


file_path = "/Users/camilla/Python-/Python--1/Восьмая лаба питон/tv_schedule.txt" #Считываем данные из файла
tv_schedule = read_schedule_from_file(file_path)

"""Поиск передач по дню и времени (A)"""
def get_programs_by_day_and_time(schedule, day, start_time, end_time):
    programs = [
        program["наименование"]
        for program in schedule
        if program["день"] == day and start_time <= program["время"] <= end_time
    ]
    return programs


day = input("Введите день: ")
start_time = input("Введите время начала передачи (00:00 формат): ")
end_time = input("Введите время окончания: ")

"""Пример использования функции (A)"""
result = get_programs_by_day_and_time(tv_schedule, day, start_time, end_time)
print("Программы в", day, "с", start_time, "до", end_time, ":", *result)

"""Функция (B): Поиск передач, повторяющихся в одно и то же время"""
def find_repeated_programs(schedule):
    time_programs = {}
    for program in schedule:
        key = (program["время"], program["наименование"])
        if key in time_programs:
            time_programs[key].append(program["день"])
        else:
            time_programs[key] = [program["день"]]

    repeated = {
        key: days for key, days in time_programs.items() if len(days) > 1
    }
    return repeated

"""Пример использования функции (B)"""
repeated_programs = find_repeated_programs(tv_schedule)
if repeated_programs:
    for (time, name), days in repeated_programs.items():
        print(f"Программа '{name}' транслируется в {time}, {', '.join(days)}")
else:
    print("Повторяющиеся программы не найдены.")

"""Функция (C): Получение информации о фильме"""
def get_movie_info(schedule, movie_name):
    movie_info = [
        program
        for program in schedule
        if program["наименование"].lower() == movie_name.lower()
    ]
    if movie_info:
        return movie_info
    else:
        return "Данного фильма нет в распичании на этой неделе."

"""Пример использования функции (C)"""
movie_name = "Крысий мир"
info = get_movie_info(tv_schedule, movie_name)
if isinstance(info, str):
    print(info)
else:
    for movie in info:
        print(movie)

"""
Программы в понедельник с 17:00 до 19:00: ['Крысий мир']
Программа 'Крысий мир' транслируется в 18:00, Понедельник, Вторник
{'день': 'Понедельник', 'время': '18:00', 'канал': 'Зоомир', 'тип': 'Документальный фильм', 'наименование': 'Крысий мир'}
{'день': 'Вторник', 'время': '18:00', 'канал': 'Зоомир', 'тип': 'Документальный фильм', 'наименование': 'Крысий мир'}
"""