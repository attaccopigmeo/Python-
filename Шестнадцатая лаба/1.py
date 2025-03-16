"""
Дана вершина A1 непустого стека. Извлечь из стека первый (верхний) элемент и
вывести его значение D, а также ссылку A2 на новую вершину стека. Если после извлечения
элемента стек окажется пустым, то положить A2 = null. После извлечения элемента из стека
освободить ресурсы, используемые этим элементом, вызвав его метод Dispose.
"""
# Положить значение A2= None!!!!
import gc
from random import randint


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack: 
    def __init__ (self): 
        self.head = None 
    
    def isempty(self): 
        if self.head == None: 
            return True 
        else: 
            return False
        
    def push(self, data): 
        if self.head == None: 
            self.head = Node(data) 
        else: 
            newnode = Node(data) 
            newnode.next = self.head 
            self.head = newnode 
    
    def pop(self): 
        if self.isempty(): 
            return None 
        else: 
            poppednode = self.head 
            self.head = self.head.next 
            poppednode.next = None 
            return poppednode.data 
    
    def peek(self): 
        if self.isempty(): 
            return None 
        else: 
            return self.head.data


n = int(input("Введите кол-во эл-ов списка: "))
stack = Stack()
# заполняем список случайными числами от 1 до 10
for _ in range(n):
    stack.push(randint(1, 10))

print("Вершина стека:", stack.pop())
gc.collect() # вызываем Dispose
A2 = stack.head
print("Ссылка на новую вершину", stack.head)