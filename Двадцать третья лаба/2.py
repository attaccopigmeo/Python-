"""Дано число N (> 0) и набор из N чисел. Отсортировать исходный набор чисел,
создав для него бинарное дерево. Вывести корень P1 полученного дерева, а также
отсортированный набор чисел (для вывода набора чисел выполнить перебор вершин дерева в
инфиксном порядке)."""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def position_item(p, item):
    # если элемента не оказалось, создаём его
    if p is None:
        return Node(item)
    # если элемент меньше или равен значению текущего узла, пробуем спуститься влево
    if item <= p.data:
        p.left = position_item(p.left, item)
    # иначе - вправо
    else:
        p.right = position_item(p.right, item)
    # в любом случае оставляем существующий элемент на месте
    return p


def print_infix(p):
    if p is None:
        return
    print_infix(p.left)
    print(p.data, end=' ')
    print_infix(p.right)


if __name__ == '__main__':
    with open('Двадцать третья лаба/2.txt', 'r') as f:
        arr = list(map(int, f.readline().split()))
    root = None
    for item in arr:
        root = position_item(root, item)
    print('Отсортированный массив:', end=' ')
    print_infix(root)
    print() # чтобы завершить строку