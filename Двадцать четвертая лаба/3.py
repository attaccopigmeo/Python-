"""Ученые изучают поведение птиц, вьющих гнезда на бинарном дереве, и хотят
разместить в его узлах камеры. Каждая камера может обозревать узел, в котором она
расположена, а также непосредственного предка и непосредственных потомков этого узла. По
заданному бинарному дереву требуется определить, какое минимальное количество камер
потребуется ученым для того, чтобы полностью покрыть наблюдением все узлы дерева."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.camera = False


class Tree:
    def __init__(self, root):
        self.root = root


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
    ax.scatter(x, y, s=500, c='green' if root.camera else 'red', edgecolors='black', linewidths=1.5)
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
    
    plot_binary_tree(tree.root, ax, x=0, y=0, dx=20.0, dy=1.0)
    
    plt.title("Бинарное дерево", pad=20)
    plt.tight_layout()
    plt.show()


CAMERA = 0 # имеется камера
COVERED_BY_CHILD = 1 # узел покрыт потомком
NOT_COVERED = 2 # узел не покрыт (и нужно добавить камеру в родителя)


def find_solution(node):
    cameras = 0
    status = COVERED_BY_CHILD

    if node is not None: # пустые узлы считаем покрытыми потомками
        left_status, left_cameras = find_solution(node.left)
        right_status, right_cameras = find_solution(node.right)

        cameras = left_cameras + right_cameras

        # если хотя бы один из потомков не покрыт, нужно покрыть его камерой в текущем узле
        if left_status == NOT_COVERED or right_status == NOT_COVERED:
            cameras += 1
            status = CAMERA
            node.camera = True
        # если хотя бы в одном из потомков имеется камера, узел покрыт
        elif left_status == CAMERA or right_status == CAMERA:
            status = COVERED_BY_CHILD
        # иначе узел не покрыт
        else:
            status = NOT_COVERED
    
    return status, cameras


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

    root_status, cameras = find_solution(tree.root)
    if root_status == NOT_COVERED:
        cameras += 1 # нужно покрыть корень
        tree.root.camera = True
    draw_binary_tree(tree)
    print('Требуемое количество камер:', cameras)