"""
Двое играют в игру. На столе лежат семь монет по 2 рубля и семь монет по 1 рублю.
За один ход разрешается взять монеты на сумму не более трех рублей. Забравший последнюю
монету выигрывает.
"""


class Game():
    def __init__(self, two_rub, one_rub):
        self.two_rub = two_rub
        self.one_rub = one_rub

    def make_move(self, two_rub, one_rub):
        if two_rub > self.two_rub or one_rub > self.one_rub:
            return False
        if 2 * two_rub + one_rub > 3:
            return False
        self.two_rub -= two_rub   
        self.one_rub -= one_rub
        return True

    def is_end(self):
        return self.two_rub == 0 and self.one_rub == 0


if __name__ == '__main__':
    game = Game(7, 7)
    while True:
        print("Текущее кол-во монет:", game.two_rub, game.one_rub)
        two_rub = int(input("Введите сколько хотите забрать 2-х рублевых монет: "))
        one_rub = int(input("Введите сколько хотите забрать 1-х рублевых монет: "))
        success = game.make_move(two_rub, one_rub)
        if not success:
            print("Такой ход невозможен, попробуйте еще раз.")
            continue
        if game.is_end():
            print("Вы победили.")
            break
        else:
            print("Текущее кол-во монет:", game.two_rub, game.one_rub)
        game.make_move(min(game.two_rub, 1), min(game.one_rub, 1))
        if game.is_end():
            print("Компьютер победил.")
            break