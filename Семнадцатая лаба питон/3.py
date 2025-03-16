"""
Даны ссылки A1, A2 и A3 на первый, последний и текущий элементы двусвязного
списка, содержащего не менее пяти элементов. Включить в класс IntList (см. задание
Dynamic59) функцию DeleteCurrent целого типа (без параметров), удаляющую из списка
текущий элемент и возвращающую его значение. После удаления элемента текущим
становится следующий элемент или, если следующего элемента не существует, последний
элемент списка. Метод DeleteCurrent также вызывает для удаленного элемента метод Dispose.
С помощью метода DeleteCurrent удалить из исходного списка пять элементов и вывести их
значения. Вывести также ссылки на первый, последний и текущий элементы
преобразованного списка (для пустого списка вывести три константы null).
"""

from random import randint
import gc


class Node:   
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None


class IntList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

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

    def delete_current(self):
        if self.current is None:
            return None
        value = self.current.data
        if self.current.prev is not None:
            self.current.prev.next = self.current.next
        #Тогда текущий эл. явл. начальным
        else:
            self.head = self.current.next
        if self.current.next is not None:
            self.current.next.prev = self.current.prev
            self.current = self.current.next
        #Тогда текущий эл. явл. конечным
        else:
            self.tail = self.current.prev
            self.current = self.tail
        gc.collect()
        return value

def createlist(n):
    lst = IntList()
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
    n = int(input("Введите размер списка: "))
    lst = createlist(n)
    print("Список:")
    printlist(lst)
    lst.current = lst.head.next #Текущим будем считать второй эл.
    print("Удаленные элементы:")
    for _ in range(5):
        print(lst.delete_current())
    print("Голова:", lst.head)
    print("Хвост:", lst.tail)
    print("Текущий элемент:", lst.current)