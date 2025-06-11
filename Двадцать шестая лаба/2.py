"""В текстовом файле с именем FN1 дано арифметическое выражение в инфиксной
форме. В выражении могут использоваться операции: сложение(+), вычитание(-),
умножение(*), деление нацело(/), остаток от деления(%), возведение в степень(^), а так же
целые числа из промежутка [1; 30] и переменная x. Для операции возведения в степень
показатель степени неотрицательное целое число. Постройте дерево выражения. После этого
вычислите значение выражения при заданном значении переменной x и выведите результат в
текстовый файл с именем FN2. Преобразуйте дерево, заменив все поддеревья вида x*A на A*x,
где A - некоторое поддерево, а x - переменная. Распечатайте дерево после преобразования в
файл FN2 используя многострочный формат, в котором дерево положено на бок. Каждый
уровень дерева выводите в 4-х позициях и используйте выравнивание по правому краю. При
наличии нескольких подряд идущих одинаковых операций дерево должно строиться по
правилу: операции одинакового приоритета вычисляются по порядку слева направо. Иными
словами, выражение 2+3+4+5, например, должно трактоваться как ((2+3)+4)+5, и не может
трактоваться как (2+3)+(4+5) или 2+(3+(4+5)). Результаты всех вычислений, включая
промежуточные, принадлежат типу int."""
import re
import operator


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # string: оператор, число или переменная
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __repr__(self):
        return f'Node({self.value})'

# Приоритеты операторов
PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '%': 2,
    '^': 3,
}

# Левоассоциативность (все кроме ^)
LEFT_ASSOC = {
    '+': True,
    '-': True,
    '*': True,
    '/': True,
    '%': True,
    '^': False,
}

# Поддерживаемые операторы для вычисления
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '%': operator.mod,
    '^': operator.pow,
}


# Лексер: преобразуем в токены
def tokenize(expression):
    token_pattern = r'\d+|[a-zA-Z]+|[\+\-\*/\^\%\(\)]'
    return re.findall(token_pattern, expression)


# Преобразуем инфикс в постфикс (Shunting Yard)
def infix_to_postfix(tokens):
    output = []
    stack = []

    for token in tokens:
        if token.isdigit() or token == 'x':
            output.append(token)
        elif token in PRECEDENCE:
            while (stack and stack[-1] != '(' and
                   (PRECEDENCE[stack[-1]] > PRECEDENCE[token] or
                    (PRECEDENCE[stack[-1]] == PRECEDENCE[token] and LEFT_ASSOC.get(token, True)))):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Убираем '('

    while stack:
        output.append(stack.pop())

    return output


# Построение дерева из постфиксной записи
def build_tree(postfix_tokens):
    stack = []

    for token in postfix_tokens:
        if token in OPERATORS:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))
        else:
            stack.append(Node(token))

    return stack[0]


# Вычисление дерева
def evaluate_tree(node, x_value):
    if node.value == 'x':
        return x_value
    if node.value.isdigit():
        return int(node.value)
    left_val = evaluate_tree(node.left, x_value)
    right_val = evaluate_tree(node.right, x_value)
    return OPERATORS[node.value](left_val, right_val)


# Преобразование x*A -> A*x
def transform_tree(node):
    if node is None or node.is_leaf():
        return node
    node.left = transform_tree(node.left)
    node.right = transform_tree(node.right)

    # Ищем поддеревья вида x * A -> A * x
    if node.value == '*' and node.left.value == 'x' and node.right.value != 'x':
        node.left, node.right = node.right, node.left
    return node


# Вывод дерева на бок в файл
def print_tree_sideways(node, file, indent=0):
    if node is None:
        return
    print_tree_sideways(node.right, file, indent + 4)
    file.write(' ' * indent + f'{node.value:>4}\n')
    print_tree_sideways(node.left, file, indent + 4)


def process_expression(FN1, FN2, x_value):
    with open(FN1, 'r') as f:
        expression = f.read().strip()

    # Токенизация -> Постфикс -> Дерево
    tokens = tokenize(expression)
    postfix = infix_to_postfix(tokens)
    root = build_tree(postfix)

    # Вычисление
    result = evaluate_tree(root, x_value)

    # Преобразование дерева
    root = transform_tree(root)

    # Запись результата и дерева
    with open(FN2, 'w') as f:
        f.write(f'Результат выражения при x = {x_value}: {result}\n\n')
        f.write('Дерево выражения:\n\n')
        print_tree_sideways(root, f)


if __name__ == "__main__":
    process_expression('Двадцать шестая лаба/FN1.txt', 'Двадцать шестая лаба/FN2.txt', x_value=4)
