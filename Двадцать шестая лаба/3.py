"""В первой строке текстового файла записаны целые числа, разделенные
пробелами. Создать дерево поиска, последовательно включая в него перечисленные в файле
числа. После этого необходимо, привести дерево к АВЛ-сбалансированному виду, выполнив
для LR-поворот. Известно, что требуется не более одного такого поворота. Вывести корень
полученного дерева."""
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f"Node({self.key})"


# Вставка значения в бинарное дерево поиска (BST)
def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # После вставки обновляем высоту узла
    root.height = 1 + max(height(root.left), height(root.right))
    return root


# Получение высоты узла (для балансировки)
def height(node):
    return node.height if node else 0


# Вычисление баланс-фактора узла
def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0


# Левый поворот (используется в балансировке)
def left_rotate(z):
    y = z.right
    T2 = y.left

    # Выполняем поворот
    y.left = z
    z.right = T2

    # Обновляем высоты
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y


# Правый поворот (используется в балансировке)
def right_rotate(z):
    y = z.left
    T3 = y.right

    # Выполняем поворот
    y.right = z
    z.left = T3

    # Обновляем высоты
    z.height = 1 + max(height(z.left), height(z.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y


# Выполнение одного LR-поворота (лево-правого)
def perform_LR_rotation(root):
    # Проверка необходимости LR-поворота:
    # если левое поддерево перегружено вправо (левый перекос с правым перекосом в левом поддереве)
    if balance_factor(root) > 1 and balance_factor(root.left) < 0:
        # Сначала левый поворот в левом поддереве
        root.left = left_rotate(root.left)
        # Затем правый поворот в корне
        return right_rotate(root)
    return root


# Отрисовка дерева
def draw_tree(root, title="Дерево"):
    pos = {}
    get_positions(root, 0, 0, pos)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_title(title)
    ax.axis('off')

    draw_edges(ax, root, pos) # рисуем связи
    draw_nodes(ax, pos) # рисуем узлы

    plt.show()


# Расчёт координат для узлов дерева
def get_positions(node, x, y, pos, x_offset=1):
    if node is None:
        return x

    # Рекурсивный обход в порядке LNR (inorder) для правильного расположения по горизонтали
    x = get_positions(node.left, x, y - 1, pos, x_offset)
    pos[node] = (x, y)
    x += x_offset
    x = get_positions(node.right, x, y - 1, pos, x_offset)
    return x


# Отрисовка рёбер между узлами
def draw_edges(ax, node, pos):
    if node is None:
        return
    if node.left:
        x1, y1 = pos[node]
        x2, y2 = pos[node.left]
        ax.plot([x1, x2], [y1, y2], 'k-') # линия от родителя к левому потомку
        draw_edges(ax, node.left, pos)
    if node.right:
        x1, y1 = pos[node]
        x2, y2 = pos[node.right]
        ax.plot([x1, x2], [y1, y2], 'k-') # линия от родителя к правому потомку
        draw_edges(ax, node.right, pos)


# Отрисовка самих узлов
def draw_nodes(ax, pos):
    for node, (x, y) in pos.items():
        ax.text(x, y, str(node.key), ha='center', va='center',
                bbox=dict(boxstyle='circle', facecolor='lightblue'))


# Основная функция обработки: чтение чисел, построение и балансировка дерева
def process_file(filename):
    with open(filename, 'r') as f:
        numbers = list(map(int, f.readline().split()))

    # Строим бинарное дерево поиска (BST)
    root = None
    for num in numbers:
        root = insert(root, num)

    draw_tree(root, "До LR-поворота") # отрисовка до балансировки

    root = perform_LR_rotation(root) # балансировка дерева

    draw_tree(root, "После LR-поворота") # отрисовка после LR-поворота

    print(f"Корень после LR-поворота: {root.key}")


if __name__ == "__main__":
    process_file("Двадцать шестая лаба/3.txt")