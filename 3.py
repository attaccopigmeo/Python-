"""
Даны две очереди с вершинами Head1 и Head2, элементами которых являются целые числа. Числа в очередях располагаются по возрастанию. Объединить две очереди в одну, сохранив порядок по возрастанию. Использовать только допустимые операции работы с очередью (Enqueue, Dequeue).
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

h = Queue()
while not h1.isempty() or not h2.isempty(): # пока не опустошатся обе очереди
    # если в первой очереди дата раньше даты во второй
    # или вторая очередь пустая
    if not h1.isempty() and (h2.isempty() or h1.top() <= h2.top()): 
        h.enqueue(h1.top()) # то выбираем элемент первой очереди
        h1.dequeue()
    # если во второй очереди дата раньше даты во первой
    # или первая очередь пустая
    elif not h2.isempty() and (h1.isempty() or h2.top() <= h1.top()):
        h.enqueue(h2.top())
        h2.dequeue()

# выводим очередь
print("Элементы итоговой очереди:")
while not h.isempty():
     # strftime выводит дату в заданном формате
     # здесь задан формат ДД.ММ.ГГГГ
    print(h.dequeue().strftime('%d.%m.%Y'))
print()