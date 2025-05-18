"""Реализовать для бинарного дерева интерфейс итератора, который будет возвращать
значения элементов, находящихся в узлах дерева, в порядке "право-корень-лево".
Преобразовывать дерево в список или иную структуру данных нельзя, рекурсию использовать
запрещается."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root
        self.stack = []
    
    def __iter__(self):
        node = self.root
        self.stack = []
        # изначально наполняем стек, идя по дереву вправо
        while node is not None:
            self.stack.append(node)
            node = node.right
        return self
    
    def __next__(self):
        # если в стеке ничего не осталось, всё обошли
        if len(self.stack) == 0:
            raise StopIteration
        # вытаскиваем очередной узел из стека
        node = self.stack.pop()
        # если возможно, спускаемся из текущего узла влево и идём вправо до конца
        if node.left is not None:
            cur = node.left
            while cur is not None:
                self.stack.append(cur)
                cur = cur.right
        return node.data


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
    tree = Tree(nodes[0])
    del nodes
    
    for item in tree:
        print(item, end=' ')
    print()
