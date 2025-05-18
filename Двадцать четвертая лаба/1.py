"""Преобразовать двусвязный список в бинарное дерево поиска без использования
дополнительной памяти (создания новых объектов). Корнем дерева должен стать элемент
списка, находящийся в его середине, а само дерево должно иметь наименьшую возможную
высоту. При преобразовании поля left и right узлов бинарного дерева рассматриваются
эквивалентными полям prev и next узлов двусвязного списка. Вывести исходный список и
получившееся дерево."""
from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None # оно же self.prev
        self.right = None # оно же self.next


def find_mid(head):
    length = 0
    cur = head
    while cur is not None:
        length += 1
        cur = cur.right
    mid = length // 2
    cur = head
    for i in range(mid):
        cur = cur.right
    return cur


# наиболее оптимальный способ - на каждом этапе выделять элемент посередине
# далее рассматривать части списка слева и справа по отдельности
# полученные деревья становятся левым и правым поддеревом среднего элемента
def transform(head):
    mid = find_mid(head)
    if mid.left is not None:
        mid.left.right = None
        mid.left = transform(head)
    if mid.right is not None:
        mid.right.left = None
        mid.right = transform(mid.right)
    return mid


def print_tree(root):
    queue = [root]
    while len(queue) > 0:
        cur = queue[0]
        print(cur.data, end=' ')
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)
        queue = queue[1:]


if __name__ == '__main__':
    n = int(input('Введите длину списка: '))
    lst = Node(randint(1, 10))
    for _ in range(n - 1):
        new_node = Node(randint(1, 10))
        new_node.right = lst
        lst.left = new_node
        lst = new_node
    
    print('Исходный список:', end=' ')
    cur = lst
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.right
    print()

    tree = transform(lst)
    print('Получившееся дерево:', end=' ')
    print_tree(tree)
    print()