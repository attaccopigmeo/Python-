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


class Game():
    def __init__(self, rocks, players):
        self.rocks = rocks
        self.players = players
        
    def game_loop(self):
        while True:
            for player in self.players:
                if self.is_end(player):
                    return player.name
                player.make_move(self)
                print("Текущее кол-во камней:", *self.rocks)

    def is_end(self, player):
        for i in range(len(self.rocks)):
            if i == player.last_move:
                continue
            if self.rocks[i] > 0:
                return False
        return True
    

class Player():
    def __init__(self):
        self.name = 'Игрок'
        self.last_move = None
    
    def make_move(self,game):
        while True:
            move = int(input("Введите номер кучки, откуда хотите забрать камень: "))
            if move == self.last_move or game.rocks[move] == 0:
                print("Такой ход невозможен, попробуйте еще раз.")
                continue
            game.rocks[move] -= 1
            self.last_move = move
            break


class Computer():
    def __init__(self):
        self.name = 'Компьютер'
        self.last_move = None
    
    def make_move(self,game):
        for i in range(len(game.rocks)): #проходим по кучкам камней
            if self.last_move != i and game.rocks[i] > 0:
                game.rocks[i] -= 1
                self.last_move = i
                break

    
if __name__ == '__main__':
    game = Game([10, 11, 12], [Player(), Computer()])
    loser = game.game_loop()
    print(loser, "проиграл.")