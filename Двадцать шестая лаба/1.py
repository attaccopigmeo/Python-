"""В текстовом файле с именем filename дано арифметическое выражение в
префиксной форме. Операндами в выражении являются целые числа из промежутка от 0 до 9.
Используемые операции: сложение (+), вычитание (-), умножение (*), деление нацело (/),
целочисленный остаток от деления (%) и возведение в степень (^). Постройте дерево,
соответствующее данному выражению. Знаки операций кодируйте числами: сложение(-1),
вычитание(-2), умножение(-3), деление(-4), остаток от деления(-5), возведение в степень (-6).
Преобразуйте дерево так, чтобы в нем не было операций возведения в степень (замените
поддеревья, в которых есть возведение в степень, значением данного поддерева). Выведите
указатель на корень полученного дерева."""
import matplotlib.pyplot as plt
import numpy as np


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # int: операнд (0-9) или операция (-1 - -6)
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.value})'


OPERATOR_CODES = {
    '+': -1,
    '-': -2,
    '*': -3,
    '/': -4,
    '%': -5,
    '^': -6,
}

REVERSE_CODES = {v: k for k, v in OPERATOR_CODES.items()}


def parse_expression(tokens):
    token = tokens.pop(0)

    if token in OPERATOR_CODES:
        node = Node(OPERATOR_CODES[token])
        node.left = parse_expression(tokens)
        node.right = parse_expression(tokens)
        return node
    else:
        return Node(int(token))


def evaluate_power_subtrees(node):
    if node is None:
        return None

    node.left = evaluate_power_subtrees(node.left)
    node.right = evaluate_power_subtrees(node.right)

    if node.value == -6:  # ^
        base = node.left.value
        exp = node.right.value
        result = base ** exp
        return Node(result)
    return node


def get_label(value):
    """Преобразуем числовой код обратно в символ операции, если нужно."""
    return REVERSE_CODES.get(value, str(value))


# рисование дерева
def draw_tree(root):
    def _get_positions(node, depth=0, pos_dict={}, x=0):
        """Рекурсивно вычисляет позицию узлов для рисования."""
        if node is None:
            return 0, pos_dict

        if node.left:
            left_width, pos_dict = _get_positions(node.left, depth + 1, pos_dict, x)
        else:
            left_width = 0

        node_x = x + left_width
        pos_dict[node] = (node_x, -depth)

        if node.right:
            right_width, pos_dict = _get_positions(node.right, depth + 1, pos_dict, node_x + 1)
        else:
            right_width = 0

        width = max(1, left_width + right_width)
        return width, pos_dict

    def _draw_edges(ax, node, pos_dict):
        if node.left:
            x1, y1 = pos_dict[node]
            x2, y2 = pos_dict[node.left]
            ax.plot([x1, x2], [y1, y2], 'k-')
            _draw_edges(ax, node.left, pos_dict)
        if node.right:
            x1, y1 = pos_dict[node]
            x2, y2 = pos_dict[node.right]
            ax.plot([x1, x2], [y1, y2], 'k-')
            _draw_edges(ax, node.right, pos_dict)

    def _draw_nodes(ax, pos_dict):
        for node, (x, y) in pos_dict.items():
            ax.text(x, y, get_label(node.value), ha='center', va='center',
                    bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='circle'))

    fig, ax = plt.subplots(figsize=(10, 5))
    _, positions = _get_positions(root)
    _draw_edges(ax, root, positions)
    _draw_nodes(ax, positions)

    ax.set_aspect('equal')
    ax.axis('off')
    plt.title("Дерево арифметического выражения")
    plt.show()


# чтение и обработка
def process_expression_file(filename):
    with open(filename, 'r') as file:
        tokens = file.read().strip().split()

    root = parse_expression(tokens)
    root = evaluate_power_subtrees(root)
    return root


if __name__ == "__main__":
    root = process_expression_file('Двадцать шестая лаба/1.txt')
    print("Корень дерева:", root)
    draw_tree(root)
