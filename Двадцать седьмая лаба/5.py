"""Реализовать определение класса (поля, свойства, конструкторы, перегрузку оператора вывода
для вывода полей, заданный метод согласно варианту). Добавить перегруженные операторы.
Протестировать все операторы и методы, включая конструкторы, не забывайте проверять
вводимые пользователем данные на корректность!
Название класса: Time
Поля: hours minutes
Метод: Вычитание времени (величины типа Time) из объекта типа Time (учесть, что возможен переход)
    в предыдущие сутки). Результат должен быть типа Time.
Перегружаемые операторы: 
    Операции приведения типа:
    int – результатом является
    количество часов (минуты
    отбрасываются);
    boolean – результатом является
    true, если часы и минуты не равны
    нулю, и false в противном случае.
    Бинарные операции:
    - положительное целое число
    минут к времени.
    + Time t – сложить два времени"""

class Time:
    def __init__(self, time):
        self.hours, self.minutes = [int(i) for i in time.split(':')]
    
    def subtract(self, other):
        return self - (other.hours * 60 + other.minutes)
    
    def __add__(self, other):
        hours, minutes = divmod(self.minutes + other.minutes, 60)
        hours = (hours + self.hours + other.hours) % 24
        return self.__class__(str(hours) + ':' + str(minutes))
    
    def __sub__(self, minutes):
        hours, minutes = divmod(self.minutes - minutes, 60)
        hours = (self.hours + hours) % 24
        return self.__class__(str(hours) + ':' + str(minutes))
    
    def __int__(self):
        return self.hours
    
    def __bool__(self):
        return (self.hours != 0) and (self.minutes != 0)
    
    def __str__(self):
        return f'{self.hours}:{self.minutes:02}'


if __name__ == '__main__':
    time = Time(input("Введите время в формате ЧЧ:ММ>"))
    print('Время:', str(time))
    print('Часы:', int(time))
    print('Время не нулевое?', bool(time))
    time2 = Time(input('Введите время, которое нужно добавить в формате ЧЧ:ММ>'))
    print('Время после добавления:', str(time + time2))
    time2 = Time(input('Введите время, которое нужно вычесть в формате ЧЧ:ММ>'))
    print('Время после вычитания:', str(time.subtract(time2)))
    minutes = int(input('Введите количество минут, которое нужно вычесть: '))
    print('Время после вычитания:', str(time - minutes))