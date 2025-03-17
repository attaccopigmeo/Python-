"""
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вывести элементы списка, перечисляя их от последнего к первому.
"""
# Старый список выводить, не создавая новый

from random import randint


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)
    
    
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

def printreversed(node):
    if node is None:
        return
    printreversed(node.next)
    print(node.data, end=' ')


if __name__ == '__main__':
    n = int(input("Введите кол-во эл-ов списка: "))
    lst = LinkedList()
    # заполняем список случайными числами от 1 до 10
    for _ in range(n):
        lst.insertAtEnd(randint(1, 10))
    print('Элементы списка:', end=' ')
    cur = lst.head
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print()
    # создадим перевёрнутый список
    print('Перевернутый список:', end=' ')
    printreversed(lst.head)
