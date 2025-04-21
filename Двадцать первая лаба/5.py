"""
Расширить класс двусвязного циклического списка с барьерным элементом из лабораторной работы №16 интерфейсом итератора. Итератор должен возвращать все элементы списка в обратном порядке без остановки. Вместо значения барьерного элемента итератор должен возвращать строку "barrier"
"""

from random import randint

class Node:   
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None


class IntListB:
    def __init__(self):
        self.current = None
        self.barrier = Node('barrier')
        # барьерный элемент считается следующим после последнего и предыдущим перед первым

    def push_front(self, new_data):  
        new_node = Node(new_data)
        new_node.prev = self.barrier
        if self.barrier.prev is not None: # добавляемый элемент НЕ первый
            # прежний первый элемент идёт после нового
            new_node.next = self.barrier.next
            new_node.next.prev = new_node
        else: # добавляемый элемент первый
            # новый элемент оказывается и последним
            new_node.next = self.barrier
            self.barrier.prev = new_node
        self.barrier.next = new_node
        
    
    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.barrier
        if self.barrier.next is not None: # добавляемый элемент НЕ первый
            # прежний последний элемент идёт перед новым
            new_node.prev = self.barrier.prev
            new_node.prev.next = new_node
        else: # добавляемый элемент первый
            # новый элемент оказывается и первым
            new_node.prev = self.barrier
            self.barrier.next = new_node
        self.barrier.prev = new_node

    def to_first(self):
        self.current = self.barrier.next # первый элемент следует за барьерным
    
    def to_next(self):
        if self.current != self.barrier:
            self.current = self.current.next

    def set_data(self, d):
        if self.current != self.barrier: # барьерному элементу значение не присваивается
            self.current.data = d
    
    def is_barrier(self):
        return self.current == self.barrier
    
    def __iter__(self):
        self.current = self.barrier.prev # устанавливаем итератор в конец списка
        return self
    
    def __next__(self):
        x = self.current.data
        self.current = self.current.prev
        return x


def createlist(n):
    lst = IntListB()
    for _ in range(n):
        lst.push_back(randint(1, 10))
    return lst

def printlist(lst):
    lst.to_first()
    while not lst.is_barrier():
        print(lst.current.data, end=' ')
        lst.to_next()
    print() # переходим на новую строку

if __name__ == '__main__':
    n = int(input("Введете размер списка: "))
    lst = createlist(n)
    print("Список:")
    printlist(lst)
    print("Список в обратном порядке:")
    for x in lst:
        if x == 'barrier':
            break
        print(x, end=' ')
    print()