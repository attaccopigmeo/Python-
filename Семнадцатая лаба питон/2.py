"""
Для двух непустых двусвязных списков даны следующие объекты: A1 и A2 —
начало и конец первого списка, A0 — один из элементов второго списка. Объединить
исходные списки, поместив все элементы первого списка (в том же порядке) перед данным
элементом второго списка, и вывести ссылки на первый и последний элементы объединенного
списка. Новые объекты типа Node не создавать.
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

    def insert(self, a, lst):
        if a.prev is None:
            self.head = lst.head
        else:
            a.prev.next = lst.head
        lst.head.prev = a.prev
        a.prev = lst.tail
        lst.tail.next = a

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
    n = int(input("Введите размер первого списка: "))
    lst1 = createlist(n)
    print("Список первый:")
    printlist(lst1)
    m = int(input("Введите размер второго списка: "))
    lst2 = createlist(m)
    print("Список второй:")
    printlist(lst2)
    lst2.insert(lst2.tail, lst1)
    print("Голова и хвост объединенного списка:", lst2.head, lst2.tail)
    print("Объединенный список:")
    printlist(lst2)