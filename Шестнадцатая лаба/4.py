"""
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вставить значение M после каждого третьего элемента списка, и вывести ссылку на последний
элемент полученного списка P2.
"""
from random import randint


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
class LinkedList: 
    def __init__ (self): 
        self.head = None
        
    def push(self, new_data): 
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
#добавление элемента в начало списка:
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
#вставка в конец списка
    def insertAtEnd(self, data): 
        new_node = Node(data) 
        if self.head is None: 
            self.head = new_node 
            return 
        current_node = self.head 
        while(current_node.next): 
            current_node = current_node.next 
        current_node.next = new_node

    # вставка после заданного узла
    def insert_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        return new_node


n = int(input("Введите кол-во эл-ов списка: "))
lst = LinkedList()
# заполняем список случайными числами от 1 до 10
for _ in range(n):
    lst.insertAtEnd(randint(1, 10))

m = int(input("Введите число M: "))
cur = lst.head
idx = 1
while cur is not None:
    # если текущий номер кратен 3, то вставим M после него
    if idx % 3 == 0:
        cur = lst.insert_after(cur, m)
    cur = cur.next
    idx += 1 # переход к следующему индексу

print('Элементы списка:', end=' ')
cur = lst.head
end = None # здесь после окончания цикла будет последний элемент
while cur is not None:
    print(cur.data, end=' ')
    end = cur # сохраняем текущий элемент как последний просмотренный
    cur = cur.next
print()
print('Ссылка на последний элемент:', end)