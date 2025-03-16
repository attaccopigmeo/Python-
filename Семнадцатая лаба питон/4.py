"""
Даны ссылки A1 и A2 на барьерный и текущий элементы двусвязного списка.
Включить в класс IntListB (см. задание Dynamic74) процедуры ToFirst (делает текущим
первый элемент списка), ToNext (делает текущим следующий элемент в списке), SetData(D)
(присваивает текущему элементу списка значение D целого типа, если данный элемент не
является барьерным) и функцию IsBarrier логического типа (возвращает true, если текущий
элемент списка является его барьерным элементом, и false в противном случае). Методы
ToFirst, ToNext и IsBarrier не имеют параметров. Параметр D метода SetData является входным
параметром целого типа. С помощью этих методов присвоить нулевые значения элементам
исходного списка с нечетными номерами и вывести количество элементов в списке, а также
ссылку на новый текущий элемент списка (текущим элементом списка должен стать его
барьерный элемент). Нумерация ведется от первого элемента списка; барьерный элемент не
нумеруется и не учитывается при подсчете элементов.
"""

from random import randint


class Node:   
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None


class IntListB:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.barrier = None

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

    def to_first(self):
        self.current = self.head
    
    def to_next(self):
        self.current = self.current.next

    def set_data(self, d):
        

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
    print("Список первый:")
    printlist(lst)
    