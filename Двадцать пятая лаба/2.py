"""Для данного текста написать программу с кодом Хаффмана. Для каждого символа должен
быть указан его код, а также должно быть приведено дерево кодирования выполненное в
«вручную». Вычислить размер сообщения при равномерном кодировании и при кодировании с
помощью построенного кода Хаффмана."""
"""НА ДВОРЕ ТРАВА, НА ТРАВЕ ДРОВА"""


class Node:
    def __init__(self, chars, freq):
        self.chars = chars
        self.freq = freq
        self.left = None
        self.right = None


class HuffmanTree:
    def __init__(self, msg):
        self.freq = self._count_freq(msg)
        self.root = self._make_tree()

    def encode_char(self, ch):
        encoding = ''
        # Спускаемся по дереву, пока не дойдём до листа
        # Если спустились влево, дописываем к коду 0, иначе 1
        cur = self.root
        while cur.left or cur.right:
            if cur.left is not None and ch in cur.left.chars:
                encoding += '0'
                cur = cur.left
            elif cur.left is not None and ch in cur.right.chars:
                encoding += '1'
                cur = cur.right
        return encoding

    def encode_text(self, text):
        # для кодирования текста кодируем каждый символ
        encoding = ''
        for ch in text:
            encoding += self.encode_char(ch)
        return encoding
    
    def get_char_encodings(self):
        # получаем коды всех символов
        encodings = {}
        for ch in self.freq:
            encodings[ch] = self.encode_char(ch)
        return encodings
    
    # с нижнего подчёркивания начинаются методы, которые доступны только внутри класса

    def _count_freq(self, msg):
        # Подсчитываем частоты каждого символа
        self.freq = {}
        for ch in msg:
            if ch in self.freq:
                self.freq[ch] += 1
            else:
                self.freq[ch] = 1
        return self.freq

    def _make_tree(self):
        nodes = []
        # Создаём листья
        for ch in self.freq:
            nodes.append(Node(ch, self.freq[ch]))
        # Далее для двух узлов с наименьшей частотой создаём новый узел,
        # потомками которого будут эти узлы
        # Частота этого узла равна сумме частот двух узлов
        # Так повторяем, пока не останется один узел без предка - он будет корнем
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.freq)
            node1 = nodes.pop(0)
            node2 = nodes.pop(0)
            new_node = Node(node1.chars + node2.chars, node1.freq + node2.freq)
            new_node.left = node1
            new_node.right = node2
            nodes.append(new_node)
        return nodes[0]


def uniform_encoding_len(msg):
    chars = {ch for ch in msg}
    m = 0
    while 2 ** m < len(chars):
        m += 1
    return m * len(msg)


if __name__ == '__main__':
    msg = input("Введите сообщение: ")
    tree = HuffmanTree(msg)
    print('Коды символов:')
    for ch, code in tree.get_char_encodings().items():
        print(ch, '=>', code)
    print('Закодированное сообщение:', tree.encode_text(msg))
    print('Длина сообщения при кодировании по Хаффману:', len(tree.encode_text(msg)))
    print('Длина сообщения при равномерном кодировании:', uniform_encoding_len(msg))