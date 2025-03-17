"""
Требуется создать игру для некоторого количества игроков (правила игры описаны в задаче).
Обязательно наличие: пользовательского интерфейса, классов, компьютерного противника.
Графический интерфейс не обязателен, можно заменить текстовым.
Изначально на столе лежат три кучки из 10, 11 и 12 камней соответственно. Илья и
Костя играют в следующую игру. За один ход каждый из них может взять себе один камень из
любой кучи, кроме той, из которой он брал камень на своем предыдущем ходе (на своём
первом ходе каждый игрок может брать камень из любой кучки). Ходы игроки делают по
очереди. Проигрывает тот, кто не может сделать ход.
"""
# интерфейс через tkinter, наличие минимум 2-х классов в каждой задаче, залить все задачи за этот сем на online.psu

PLAYER = 0
COMPUTER = 1


class Game():
    def __init__(self, rocks, players):
        self.rocks = rocks
        self.last_move = [None] * players
        
    def make_move(self, player, move):
        if move < 0 or move >= len(self.rocks):
            return False
        if move == self.last_move[player]:
            return False
        if self.rocks[move] == 0:
            return False
        self.rocks[move] -= 1
        self.last_move[player] = move
        return True
    
    def is_end(self, player):
        for i in range(len(self.rocks)):
            if i == self.last_move[player]:
                continue
            if self.rocks[i] > 0:
                return False
        return True

    
if __name__ == '__main__':
    game = Game([10, 11, 12], 2)
    while True:
        print("Текущее кол-во камней:", *game.rocks)
        move = int(input("Введите номер кучки, откуда хотите забрать камень: "))
        success = game.make_move(PLAYER, move)
        if not success:
            print("Такой ход невозможен, попробуйте еще раз.")
            continue
        if game.is_end(COMPUTER):
            print("Вы победили.")
            break
        else:
            print("Текущее кол-во камней:", *game.rocks)
        for i in range(len(game.rocks)):
            if game.last_move[COMPUTER] != i and game.rocks[i] > 0:
                game.make_move(COMPUTER, i)
                break
        if game.is_end(PLAYER):
            print("Компьютер победил.")
            break