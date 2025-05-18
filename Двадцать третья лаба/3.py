"""Дано бинарное дерево и корень дерева P1. Необходимо вывести второе
максимальное значение в дереве. Решение должно иметь сложность по времени исполнения
T(n) = O(log n), где n - число вершин в дереве."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# второе максимальное значение лежит в предке самого правого элемента
# если у него нет предка, переходим влево, а затем вправо до упора
def find_second_max(root):
    # сначала спускаемся вправо до упора
    cur = root
    parent = None
    while cur.right is not None:
        parent = cur
        cur = cur.right
    # если предок есть, то возвращаем его значение:
    if parent is not None:
        return parent.data
    # иначе спускаемся влево, а затем вправо до упора
    cur = cur.left
    while cur.right is not None:
        cur = cur.right
    return cur.data


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
    print('Второе максимальное значение:', find_second_max(p1))