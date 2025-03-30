from itertools import permutations
import io


KEY_LENGTH = 6

with io.open('ДЗ дискр\\cipher27.txt', encoding='utf-8') as f:
    cipher = f.read()

with io.open('ДЗ дискр\\decoding.txt', mode='w', encoding='utf-8') as f:
    # перебираем каждый возможный код
    for key in permutations(range(KEY_LENGTH), KEY_LENGTH): # выдаёт по очереди все перестановки элементов массива
        dec_str = ''
        for i in range(0, len(cipher), KEY_LENGTH): # просматриваем блок за блоком
            block = cipher[i:i+KEY_LENGTH] # выделяем блок длины KEY_LENGTH
            dec_block = ''
            for j in range(KEY_LENGTH):
                # если очередной блок короче ключа, игнорируем номера, выходящие за границы блока
                if len(block) <= key[j]:
                    continue
                # ставим на очередную позицию символ согласно ключу
                # т.е. если в ключе на позиции k стоит j, выберем из шифровки символ на позиции j
                # и поставим его на позицию k
                dec_block += block[key[j]]
            dec_str += dec_block
        # для упрощения поиска будем выписывать только те варианты, которые начинаются на заглавную букву
        # и оканчиваются на точку
        if dec_str[0] == dec_str[0].upper() and dec_str[0] != ' ' and dec_str.strip()[-1] == '.':
            f.write(dec_str)
