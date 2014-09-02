__author__ = 'Cole'

#Copyright Cole Gosney 2014
#The 'Zerg Rush' minigame

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from random import randint

import main_game

class zergrush:
    def __init__(self):
        self.RUN = False
        self.time = 0
        self.hp = 0
        self.enemys = []
        
    def start(self):
        self.RUN = True
        self.time = 0
        self.hp = 30
        self.enemys = []
        
    def update(self):
        if self.RUN:
            self.time += 1
            self.draw()
            self.ai()
            if randint(0, 20) == 0:
                self.add_enemy()
            if self.hp <= 0:
                self.end()
            main_game.app.clock['text'] = "Time:" + str(((self.time) / 60) // 1)
        
    def draw(self):
        main_game.app.canvas.delete(ALL)

        main_game.app.canvas.create_rectangle(main_game.WIDTH / 2 - 40, main_game.HEIGHT / 2 - 40, main_game.WIDTH / 2 + 40, main_game.HEIGHT / 2 + 40)

        main_game.app.canvas.create_text(main_game.WIDTH / 2, main_game.HEIGHT / 2, text = str(self.hp) + "hp")
        
        for i in self.enemys:
            main_game.app.canvas.create_oval(i[0], i[1], i[0] + 25, i[1] + 25)

    def ai(self):
        for i in self.enemys:
            if i[0] >= main_game.WIDTH / 2 - 40 and i[0] <= main_game.WIDTH / 2 + 40 and i[1] >= main_game.HEIGHT / 2 - 40 and i[1] <= main_game.HEIGHT / 2 + 40:
                if i[2] == 40:
                    self.hp -= 2
                    i[2] = 0
                else:
                    i[2] += 1
            else:
                if i[0] < main_game.WIDTH / 2:
                    i[0] += 2
                elif i[0] > main_game.WIDTH / 2:
                    i[0] -= 2
                elif i[0] == main_game.WIDTH / 2:
                    i[0] = i[0]
                if i[1] < main_game.HEIGHT / 2:
                    i[1] += 2
                elif i[1] > main_game.HEIGHT / 2:
                    i[1] -= 2
                elif i[1] == main_game.HEIGHT / 2:
                    i[1] = i[1]

    def add_enemy(self):
        if randint(0, 1) == 0:
            self.temp_pos = [(main_game.HEIGHT / 8 * 1) - randint(0, 50), randint(0, main_game.HEIGHT), 40]
        else:
            self.temp_pos = [(main_game.HEIGHT / 8 * 7) + randint(0, 50), randint(0, main_game.HEIGHT), 40]
        self.enemys.append(self.temp_pos)

    def check(self, x, y):
        for i in self.enemys:
            if x > i[0] and x < i[0] + 25:
                if y > i[1] and y < i[1] + 25:
                    self.enemys.remove(i)

    def end(self):
        self.RUN = False
        main_game.app.point += ((self.time / 60) * 3) // 1
        main_game.app.old_point = ((self.time / 60) * 3) // 1
        main_game.app.time += 60
        main_game.app.run_once = True
        main_game.game = "bus"

app = zergrush()
