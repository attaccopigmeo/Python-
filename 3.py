"""
Даны две очереди с вершинами Head1 и Head2, элементами которых являются даты. В очереди Head1 записаны даты поступления товара в хронологическом порядке, в очереди Head2 – даты отгрузки (один элемент очереди соответствует 1 единице товара). Изначально товара на складе не было. Определить корректность записей (не возникало ли ситуации, когда количество товара на складе становилось отрицательным). Если записи корректны, то вывести количество товара на складе после всех поступлений и отгрузок. Использовать только допустимые операции работы с очередью (Enqueue, Dequeue).
"""
class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def Dequeue(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
    
    def Enqueue(self, data):
        new_node = Node(data)
        if self.isempty():
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node

    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next


n = int(input("Введите кол-во эл-ов очереди: "))
q = Queue()
# заполняем очередь случайными числами от 1 до 10
for _ in range(n):
    q.push(randint(1, 10))