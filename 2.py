"""
Даны две очереди с вершинами Head1 и Head2, элементами которых являются даты. В очереди Head1 записаны даты поступления товара в хронологическом порядке, в очереди Head2 – даты отгрузки (один элемент очереди соответствует 1 единице товара). Изначально товара на складе не было. Определить корректность записей (не возникало ли ситуации, когда количество товара на складе становилось отрицательным). Если записи корректны, то вывести количество товара на складе после всех поступлений и отгрузок. Использовать только допустимые операции работы с очередью (Enqueue, Dequeue).
"""
from datetime import date


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

    def dequeue(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.isempty():
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node
    
    def top(self):
        return self.head.data

    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next


n1 = int(input("Введите кол-во поступлений: "))
h1 = Queue()
print("Введите даты поступления в хронологическом порядке в формате ДД.ММ.ГГГГ")
for _ in range(n1):
    d, m, y = map(int, input().split('.'))
    h1.enqueue(date(y, m, d))

n2 = int(input("Введите количество отгрузок: "))
h2 = Queue()
print("Введите даты отгрузки в хронологическом порядке в формате ДД.ММ.ГГГГ")
for _ in range(n2):
    d, m, y = map(int, input().split('.'))
    h2.enqueue(date(y, m, d))

goods = 0
while not h1.isempty() or not h2.isempty(): # пока не опустошатся обе очереди
    # если в первой очереди дата раньше даты во второй
    # или вторая очередь пустая
    if not h1.isempty() and (h2.isempty() or h1.top() <= h2.top()): 
        h1.dequeue() # то выбираем элемент первой очереди
        goods += 1 # добавляем товар
    # если во второй очереди дата раньше даты во первой
    # или первая очередь пустая
    elif not h2.isempty() and (h1.isempty() or h2.top() <= h1.top()):
        h2.dequeue() # то выбираем элемент второй очереди
        goods -= 1 # удаляем товар
        if goods < 0: # если товаров оказалось отрицательное число, то записи некорректны
            break # дальше проверять смысла нет

if goods < 0: # если осталось отрицательное количество товаров, то записи некорректны
    print("Записи некорректны!")
else:
    print("Записи корректны.")
    print("Товаров осталось:", goods)