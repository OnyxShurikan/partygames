__author__ = 'Cole'

#Copyright Cole Gosney 2014
#The 'Little Bird' minigame

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from random import randint

import main_game

class littlebird:
    def __init__(self):
        self.pos = [0, 600 / 2]
        self.vel = [0, 3]
        self.pipes = []
        self.starting = False
        self.flying = False
        self.fly_timer = 0
        
    def start(self):
        self.pos = [0, 600 / 2]
        self.vel = [0, 3]
        self.pipes = []
        self.starting = True
        self.flying = False
        self.fly_timer = 0
        
    def update(self):
        self.pos[1] += self.vel[1]
        if self.flying:
            self.fly_timer += 1
            self.fly()
        self.draw()
        self.spawn_pipe()
        print(self.fly_timer)

    def draw(self):
        main_game.app.canvas.delete(ALL)
        main_game.app.canvas.create_oval(self.pos[0], self.pos[1], self.pos[0] + 25, self.pos[1] + 25, fill = "blue")
        for i in self.pipes:
            main_game.app.canvas.create_rectangle(i[0], i[1], i[2], i[3])

    def fly(self):
        self.flying = True
        if self.fly_timer >= 5:
            self.vel[1] = 5
            self.flying = False
            self.fly_timer = 0
        else:
            self.vel[1] = -6

    def spawn_pipe(self):
        if self.starting:
            self.starting = False
        else:
            pass

            

app = littlebird()
