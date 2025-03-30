import io # для корректного чтения входного файла
import heapq # приоритетная очередь


class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.children = []
    
    # определим для Node оператор <, чтобы в дальнейшем работала приоритетная очередь
    def __lt__(self, other):
        return self.freq < other.freq


# закодировать один символ
def encode_char(ch, node):
    if len(node.children) == 0:
        return ''
    for i, child in enumerate(node.children):
        if ch in child.ch:
            return (str(i) + encode_char(ch, child))

# закодировать текст
def encode_text(text, node):
    encoded = ''
    for ch in text:
        encoded += encode_char(ch, node)[::-1]
    return encoded


q = int(input("Введите размер кодирующего алфавита:"))
with io.open('ДЗ дискр\\text12.txt', encoding='utf-8') as f:
    text = f.read()

queue = []
cnt = {}

for ch in text:
    cnt[ch] = cnt.get(ch, 0) + 1 # get вернёт значение по умолчанию 0, если символа ещё нет в словаре

r = 0
for ch, freq in cnt.items():
    r += 1
    heapq.heappush(queue, Node(ch, freq))
b = r % (q - 1)
t = b
if b == 0:
    t = q - 1
elif b == 1:
    t = q

node_data = ''
freq_total = 0
children = []
for _ in range(t):
    node = heapq.heappop(queue)
    freq_total += node.freq
    node_data += node.ch
    children.append(node)
node = Node(node_data, freq_total)
node.children = children
# добавляем узел с частотой, равной суммарной частоте потомков, в очередь
heapq.heappush(queue, node)

while len(queue) > 1: # пока имеются некорневые вершины
    node_data = ''
    freq_total = 0
    children = []
    # получаем k узлов - потомков нового узла
    for _ in range(q):
        node = heapq.heappop(queue)
        freq_total += node.freq
        node_data += node.ch
        children.append(node)
    node = Node(node_data, freq_total)
    node.children = children
    # добавляем узел с частотой, равной суммарной частоте потомков, в очередь
    heapq.heappush(queue, node)
root = queue[0]

encoded = encode_text(text, root)
print('Закодированный текст:', encoded, sep='\n')

redud = 0
print('Кодировки символов:')
for ch, freq in cnt.items():
    code = encode_char(ch, root)
    print(ch, "-", encode_text(ch, root))
    redud += len(code) * freq / len(text)
print('Избыточность:', redud)
print('Изменение длины:', len(encoded) / len(text))