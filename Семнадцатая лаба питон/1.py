"""
Дана ссылка A0 на один из элементов непустого двусвязного списка. Переместить
данный элемент в конец списка и вывести ссылки на первый и последний элементы
преобразованного списка. Новые объекты типа Node не создавать, свойства Data не изменять.
"""


from random import randint


class Node:   
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, new_data):  
        new_node = Node(new_data)  
        new_node.next = self.head 
        if self.head is not None:

            self.head.prev = new_node  
        self.head = new_node
        if self.tail is None:
            self.tail = self.head
    
    def push_back(self, new_data):
        new_node = Node(new_data)  
        new_node.prev = self.tail 
        if self.tail is not None:

            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail

def movetoback(a0, lst): #перемещает элемент в конец списка
    if a0.next is None:
        return lst.head, lst.tail
    lst.tail.next = a0
    if a0.prev is None:
        lst.head = a0.next
    else:
        a0.prev.next = a0.next #после a0.prev теперь идет a0.next
    a0.next.prev = a0.prev
    a0.prev = lst.tail
    a0.next = None
    lst.tail = a0
    return lst.head, lst.tail

def createlist(n):
    lst = DoublyLinkedList()
    for _ in range(n):
        lst.push_back(randint(1, 10))
    return lst

def printlist(lst):
    cur = lst.head
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
    print()

if __name__ == '__main__':
    n = int(input("Введете размер списка: "))
    lst = createlist(n)
    print("Список:")
    printlist(lst)
    head, tail = movetoback(lst.head, lst)
    print("Новые голова и хвост:", head, tail)
    print("Список после смещения первого элемента:")
    printlist(lst)