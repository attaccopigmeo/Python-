"""
Даны ссылки A1 и A2 на начало и конец очереди, содержащей не менее пяти
элементов. Включить в класс IntQueue (см. задание Dynamic26) функцию Dequeue целого типа
(без параметров), которая извлекает из очереди первый (начальный) элемент, возвращает его
значение и вызывает для него метод Dispose. С помощью функции Dequeue извлечь из
исходной очереди пять начальных элементов и вывести их значения. Вывести также ссылки на
начало и конец результирующей очереди (если очередь окажется пустой, то эти ссылки
должны быть равны null).
"""
# В случае, когда голова None хвост должен становиться None
"""
Введите кол-во эл-ов очереди: 3
5 элементов:
9
4
4
None
None
Сслыка на голову: None
Сслыка на хвост: <__main__.Node object at 0x10447d810>
"""
import gc
from random import randint


class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            poppednode.next = None
            return poppednode.data
    
    # метод Dequeue согласно условию
    def dequeue(self):
        value = self.pop() # извлекаем элемент
        gc.collect() # вызываем метод Dispose
        return value # возвращаем значение

    def push(self, data):
        new_node = Node(data)
        if self.isempty():
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node

    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next


n = int(input("Введите кол-во эл-ов очереди: "))
q = Queue()
# заполняем очередь случайными числами от 1 до 10
for _ in range(n):
    q.push(randint(1, 10))

print('5 элементов:')
for _ in range(5):
    print(q.dequeue()) # делаем Dequeue 5 раз

print('Сслыка на голову:', q.head)
print('Сслыка на хвост:', q.tail)