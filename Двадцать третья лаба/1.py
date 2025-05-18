"""Дано бинарное дерево и корень дерева P1. Необходимо вывести содержимое
листьев дерева, перечисляя их справа налево."""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_leaves(p):
    if p is None:
        return
    # Узел является листом, если нет ни правого, ни левого потомков
    if p.left is None and p.right is None:
        print(p.data)
        return
    # Чтобы напечатать листья справа налево, сначала идём в правого потомка
    print_leaves(p.right)
    print_leaves(p.left)


if __name__ == '__main__':
    with open('Двадцать третья лаба/1.txt', 'r') as f:
        nodes = [(Node(int(x)) if x != '0' else None) for x in f.readline().split()]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        if 2 * i + 1 >= len(nodes):
            continue
        node.left = nodes[2 * i + 1]
        node.right = nodes[2 * i + 2]
    p1 = nodes[0]
    del nodes
    # отныне доступно только p1, согласно условию
    print_leaves(p1)