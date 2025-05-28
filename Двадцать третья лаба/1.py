"""Дано бинарное дерево и корень дерева P1. Необходимо вывести содержимое
листьев дерева, перечисляя их справа налево."""

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
    draw_binary_tree(p1)
    print_leaves(p1)