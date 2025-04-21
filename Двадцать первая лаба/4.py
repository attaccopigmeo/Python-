"""
Написать класс, реализующий интерфейс итератора. Класс должен принимать в конструкторе список элементов произвольного типа и позволять просмотреть его в следующем порядке: первый - последний - второй - предпоследний - ...
"""

class SimpleIter:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 0 # текущее положение итератора
        self.n = 0 # количество выведенных элементов
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n == len(self.lst):
            raise StopIteration() # если вывели все элементы, останавливаем вывод
        x = self.lst[self.idx] # получаем текущий элемент
        # переходим к следующему
        # индексы меняем по закону: 0 (первый) -> -1 (последний) -> 1 (второй) -> -2 (предпоследний) -> ...
        if self.idx >= 0:
            self.idx = -self.idx - 1
        else:
            self.idx = -self.idx
        self.n += 1
        return x


if __name__ == '__main__':
    lst = list(input("Введите список через пробел: ").split())
    it = SimpleIter(lst)
    for x in it:
        print(x)