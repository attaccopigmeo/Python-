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

class List:
    def __init__(self, head):
        self.head = head
    
    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.right
        print()


class Tree:
    def __init__(self, head):
        self.head = head
    
    def print_tree(self):
        queue = [self.head]
        while len(queue) > 0:
            cur = queue[0]
            print(cur.data, end=' ')
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
            queue = queue[1:]


import matplotlib.pyplot as plt
import numpy as np


def plot_binary_tree(root, ax=None, x=0, y=0, dx=1.0, dy=1.0, depth=1):
    """
    Рекурсивно рисует бинарное дерево, используя matplotlib.
    
    Параметры:
    - root: Корень дерева (экземпляр TreeNode)
    - ax: Объект осей matplotlib (если None, создаётся новый)
    - x, y: Координаты текущего узла
    - dx: Горизонтальный шаг между узлами (уменьшается с глубиной)
    - dy: Вертикальный шаг между уровнями
    - depth: Текущая глубина (используется для рекурсивного вычисления отступов)
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(10, 10))
        ax.set_aspect('equal')
        ax.axis('off')
    
    # Рисуем текущий узел
    ax.scatter(x, y, s=500, c='skyblue', edgecolors='black', linewidths=1.5)
    ax.text(x, y, str(root.data), ha='center', va='center', fontsize=12)
    
    # Рекурсивно рисуем левое поддерево
    if root.left is not None:
        new_dx = dx / 2  # Уменьшаем шаг для более глубоких уровней
        new_x = x - new_dx
        new_y = y - dy
        
        # Рисуем линию к левому потомку
        ax.plot([x, new_x], [y, new_y], 'gray', lw=1.5)
        
        plot_binary_tree(root.left, ax, new_x, new_y, new_dx, dy, depth + 1)
    
    # Рекурсивно рисуем правое поддерево
    if root.right is not None:
        new_dx = dx / 2
        new_x = x + new_dx
        new_y = y - dy
        
        # Рисуем линию к правому потомку
        ax.plot([x, new_x], [y, new_y], 'gray', lw=1.5)
        
        plot_binary_tree(root.right, ax, new_x, new_y, new_dx, dy, depth + 1)
    
    return ax

def draw_binary_tree(tree):
    """Основная функция для отрисовки дерева."""
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_aspect('equal')
    ax.axis('off')
    
    plot_binary_tree(tree.head, ax, x=0, y=0, dx=20.0, dy=1.0)
    
    plt.title("Бинарное дерево", pad=20)
    plt.tight_layout()
    plt.show()

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


if __name__ == '__main__':
    n = int(input('Введите длину списка: '))
    lst = Node(randint(1, 10))
    for _ in range(n - 1):
        new_node = Node(randint(1, 10))
        new_node.right = lst
        lst.left = new_node
        lst = new_node
    
    lst = List(lst)
    print('Исходный список:', end=' ')
    lst.print_list()

    tree = Tree(transform(lst.head))
    print('Получившееся дерево:', end=' ')
    tree.print_tree()
    print()
    draw_binary_tree(tree)