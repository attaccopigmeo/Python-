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
        self.current = None
        self.barrier = Node(None)
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
    lst.to_first()
    while not lst.is_barrier():
        lst.set_data(0)
        # переходим на следующий элемент дважды - то есть, перейдём на 2 элемента вперёд
        # тогда, т.к. начали с нечётного по номеру элемента, мы пройдём все нечётные по номеру элементы
        lst.to_next()
        lst.to_next()
    print("Новый список:")
    printlist(lst)