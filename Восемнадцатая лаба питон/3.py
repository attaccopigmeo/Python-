"""
Петя и Вася играют в следующую игру. У них есть клетчатый прямоугольник 50 × 101,
первым ходит Петя. Своим ходом первый игрок делит прямоугольник на два меньших одним
разрезом вдоль линии сетки. Затем второй игрок выбирает один из двух получившихся
прямоугольников, на котором будет продолжаться игра (второй прямоугольник
отбрасывается), и делит его на два меньших. Потом опять первый выбирает прямоугольник, на
котором будет продолжаться игра, и т. д. Проигрывает тот, кто не может в свой ход разрезать
прямоугольник.
"""
import tkinter as tk
from tkinter import messagebox
import random

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def make_move(self, game):
        pass

class Computer(Player):
    def __init__(self, name="Вася", color="green"):
        super().__init__(name, color)
    
    def make_move(self, game):
        game.computer_move()

class RectangleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра Петя и Вася")
        # создаём холст для рисования
        self.canvas = tk.Canvas(root, width=505, height=1010, bg="white")
        self.canvas.pack()
        
        self.rectangles = [(0, 0, 500, 1000)]  # Один прямоугольник 50x101
        self.enabled = [0] # доступен весь прямоугольник
        self.players = [Player("Петя", "red"), Computer()]
        self.current_player_index = 0
        self.draw_rectangles()
        
        self.canvas.bind("<Button-1>", self.handle_click)
        self.update_title()
    
    def draw_rectangles(self):
        self.canvas.delete("all")
        for rect in self.rectangles:
            x1, y1, x2, y2 = rect
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
    
    def handle_click(self, event):
        if isinstance(self.players[self.current_player_index], Computer):
            return
        # перебираем все прямоугольники
        for i, rect in enumerate(self.rectangles):
            x1, y1, x2, y2 = rect
            # если прямоугольник допустим для хода, и точка нажатия лежит в нём...
            if x1 <= event.x <= x2 and y1 <= event.y <= y2 and i in self.enabled:
                # ...производим ход (разбиение прямоугольника)
                self.split_rectangle(i, x1, y1, x2, y2)
                return
    
    def split_rectangle(self, index, x1, y1, x2, y2):
        width = x2 - x1
        height = y2 - y1
        
        if width > 10 and height > 10:  # Можно разрезать
            # определяем, совершаем ли разрез по X или по Y
            # разрез совершается параллельно меньшей стороне
            if width >= height:
                mid_x = (x1 + x2) // 2 # находим середину
                new_rects = [(x1, y1, mid_x, y2), (mid_x, y1, x2, y2)] # задаём новые прямоугольники
                split_line = (mid_x, y1, mid_x, y2)
            else:
                # тут аналогично
                mid_y = (y1 + y2) // 2
                new_rects = [(x1, y1, x2, mid_y), (x1, mid_y, x2, y2)]
                split_line = (x1, mid_y, x2, mid_y)
            
            del self.rectangles[index] # исключаем старый прямоугольник из списка - далее мы заменим его половинками
            self.rectangles.extend(new_rects) # добавляем новые прямоугольники в список
            # по условию задачи игрок выбирает прямоугольник, который он разрезает, и дальнейшие ходы можно делать только в нём
            # иначе говоря, последующие ходы можно делать только в новые прямоугольники - они лежат последними
            self.enabled = [len(self.rectangles) - 1, len(self.rectangles) - 2]
            # обновим картинку
            self.draw_rectangles()
            self.canvas.create_line(*split_line, fill=self.players[self.current_player_index].color, width=2)
            
            self.switch_player()
        else:
            messagebox.showinfo("Невозможно разрезать", "Этот прямоугольник слишком мал!")
    
    def switch_player(self):
        # меняем текущего игрока и заменяем подпись в заголовке
        self.current_player_index = 1 - self.current_player_index
        self.update_title()
        
        # если ходит компьютер, запускаем его алгоритм спустя 0,5 с - для того, чтобы игрок поспевал за ходом игры
        if isinstance(self.players[self.current_player_index], Computer):
            self.root.after(500, self.players[self.current_player_index].make_move, self)
        else:
            # если ходит игрок, проверяем, есть ли у него ходы
            valid_moves = [(i, rect) for i, rect in enumerate(self.rectangles) if (rect[2] - rect[0] > 10 and rect[3] - rect[1] > 10 and i in self.enabled)]
            # если ходов нет, игрок проиграл
            if not valid_moves:
                messagebox.showinfo("Игра окончена", "Вася победил!")
                self.root.quit()
    
    def update_title(self):
        self.root.title(f"Ходит: {self.players[self.current_player_index].name}")
    
    def computer_move(self):
        # ищем допустимые ходы
        valid_moves = [(i, rect) for i, rect in enumerate(self.rectangles) if (rect[2] - rect[0] > 10 and rect[3] - rect[1] > 10 and i in self.enabled)]
        # если таких нет, Вася проиграл
        if not valid_moves:
            messagebox.showinfo("Игра окончена", "Петя победил!")
            self.root.quit()
            return
        # выбираем случайный ход из допустимых и делаем его
        index, (x1, y1, x2, y2) = random.choice(valid_moves)
        self.split_rectangle(index, x1, y1, x2, y2)

if __name__ == "__main__":
    root = tk.Tk() # создаём окно
    game = RectangleGame(root) # инициализируем игру
    root.mainloop() # запускаем цикл игры
