"""
Дан текстовый файл в первой строке которого хранится число N, а во второй
строке N целых чисел. Необходимо создать упорядоченный по возрастанию список, в который
поместить все эти элементы, при этом очередной элемент вставлять в список так, чтобы не
нарушалась его упорядоченность.
"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    
class LinkedList: 
    def __init__ (self): 
        self.head = None
    
    # вставка в начало
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    # вставка в конец
    def insert_at_end(self, data): 
        new_node = Node(data) 
        if self.head is None: 
            self.head = new_node 
            return 
        current_node = self.head 
        while(current_node.next): 
            current_node = current_node.next 
        current_node.next = new_node
        
    # вставка после заданного узла
    def insert_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        return new_node


lst = LinkedList()
with open('Шестнадцатая лаба/5.txt', 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        x = int(f.readline())
        if lst.head is None or x <= lst.head.data:
            lst.insert_at_begin(x)
        else:
            cur = lst.head
            while cur is not None:
                if cur.next is None or x <= cur.next.data:
                    lst.insert_after(cur, x)
                    break

print('Элементы списка:', end=' ')
cur = lst.head
while cur is not None:
    print(cur.data, end=' ')
    cur = cur.next