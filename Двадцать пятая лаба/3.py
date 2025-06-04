"""Написать программу для шифрования и дешифрования последовательности символов
столбчатым шифром транспонирования. Должна быть возможность задания ключа пользователем"""


class ColumnarTranspositionCipher:
    def __init__(self, keyword):
        # при кодировании столбцы перестраиваются в порядке, соответствующем алфавитному порядку букв кодового слова
        self.key = sorted([(ch, i) for i, ch in enumerate(keyword.upper())])

    def encode(self, text):
        cipher = ''
        for _, pos in self.key:
            for i in range(pos, len(text), len(self.key)):
                cipher += text[i]
        return cipher
    
    def decode(self, cipher):
        table = ['\0'] * len(cipher)
        j = 0
        for _, pos in self.key:
            for i in range(pos, len(cipher), len(self.key)):
                table[i] = cipher[j]
                j += 1
        return ''.join(table)


if __name__ == '__main__':
    keyword = input('Введите кодовое слово: ')
    code = ColumnarTranspositionCipher(keyword)
    msg = input('Введите сообщение: ')
    cipher = code.encode(msg)
    print('Закодированное сообщение:', cipher)
    restored = code.decode(cipher)
    print('Раскодированное сообщение:', restored)
