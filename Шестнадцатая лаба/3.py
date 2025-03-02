"""
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вывести элементы списка, перечисляя их от последнего к первому.
"""
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
    
n = int(input("Введите кол-во эл-ов списка"))
