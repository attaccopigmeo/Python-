"""Дано число N (> 0) и набор из N чисел. Отсортировать исходный набор чисел,
создав для него бинарное дерево. Вывести корень P1 полученного дерева, а также
отсортированный набор чисел (для вывода набора чисел выполнить перебор вершин дерева в
инфиксном порядке)."""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

def draw_binary_tree(root):
    """Основная функция для отрисовки дерева."""
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_aspect('equal')
    ax.axis('off')
    
    plot_binary_tree(root, ax, x=0, y=0, dx=20.0, dy=1.0)
    
    plt.title("Бинарное дерево", pad=20)
    plt.tight_layout()
    plt.show()


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
    draw_binary_tree(root)
    print('Отсортированный массив:', end=' ')
    print_infix(root)
    print() # чтобы завершить строку