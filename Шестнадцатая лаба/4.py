"""
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вставить значение M после каждого третьего элемента списка, и вывести ссылку на последний
элемент полученного списка P2.
"""
#ИЗМЕНЕНИЕ ЗНАЧЕНИЯ УЗЛА В УКАЗАННОЙ ПОЗИЦИИ
    def updateNode(self, val, index):
        current_node = self.head 
        position = 0
        if position == index: 
            current_node.data = val
        else: 
            while(current_node != None and position != index): 
                position = position + 1 
                current_node = current_node.next 
            if current_node != None: 
                new_node.next = current_node.next 
                current_node.data = val
            else: 
                print("Index not present")
                
    #УДАЛЕНИЕ УЗЛА — ПЕРВОГО ИЛИ ПОСЛЕДНЕГО
    def remove_first_node(self): 
        if(self.head == None): 
            return 
        self.head = self.head.next
        
    def remove_last_node(self): 
        if self.head is None: 
            return 
        current_node = self.head 
        while(current_node.next.next): 
            current_node = current_node.next 
        current_node.next = None 

##    УДАЛЕНИЕ УЗЛА ПО ИНДЕКСУ
    def remove_at_index(self, index): 
        if self.head == None: 
            return 
        current_node = self.head 
        position = 0
        if position == index: 
            self.remove_first_node() 
        else: 
            while(current_node != None and position+l != index): 
                position = position+1 
                current_node = current_node.next 
            if current_node != None: 
                current_node.next = current_node.next.next 
            else: 
                print("Index not рrеsеnt")
    
    #УДАЛЕНИЕ УЗЛА NO ЗНАЧЕНИЮ
    def remove_node(self, data): 
        current_node = self.head 
        if current_node.data == data: 
            self.remove_first_node() 
            return 
        while(current_node != None and current_node.next.data != data): 
            current_node = current_node.next 
        if current_node == None: 
            return 
        else: 
            current_node.next = current_node.next.next
            
##    ОБХОД СПИСКА
    
    def printLL(self): 
        current_node = self.head 
        while(current_node): 
            print(current_node.data) 
            current_node = current_node.next
            

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node1.next = node2
node2.next = node3
print(node1.next)
d = LinkedList()
d.push(node1)
d.insertAtBegin(node2)
d.printLL()

 

 


#РЕАЛИЗАЦИЯ CTEKA
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
    
    def  pop(self): 
        if self.isempty(): 
            return None 
        else: 
            poppednode = self.head 
            self.head = self.head.next 
            poppednode.next = None 
            return poppednode.data 
    
    def    peek(self): 
        if self.isempty(): 
            return None 
        else: 
            return self.head.data

# Реализация оцереди
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

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def push(self, data):
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


d = Queue()
d.push(1)
d.push(2)
d.push(3)
d.printLL()
d.push(d.pop())
d.printLL()
