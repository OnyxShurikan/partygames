__author__ = 'Cole'

#Copyright Cole Gosney 2014
#The 'Chain Reaction' game

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from random import randint                              #Imports needed modules

import main_game                                        #Import main_game
1
class chainreaction:
    def __init__(self):
        self.RUN = False
        self.shots_left = 0
        self.shot_type = "shot"
        self.shots = []
        self.enemys = []
        self.debris = []
        self.score = 0                                  #Sets RUN to false, shots and shots_left to 0, enemys to 0, debris to 0 and score to 0

    def start(self):
        self.RUN = True
        self.shots_left = 10
        self.shots = []
        self.shot_type = "shot"
        self.enemys = []
        self.debris = []
        self.score = 0

    def update(self):
        if self.RUN:
            self.draw()
            for i in self.enemys:
                if i[2] == 0:
                    i[0] += 1.5
                    i[1] += 0
                else:
                    i[0] -= 1.5
                    i[1] += 0
            for i in self.shots:
                i[0] += 0
                i[1] += -3
                if i[0] <= 0 or i[0] >= main_game.WIDTH or i[1] <= 0 or i[1] >= main_game.HEIGHT:
                    self.shots.remove(i)
            for i in self.debris:
                if i[2] == 0:
                    i[0] += 0
                    i[1] += -3
                elif i[2] == 1:
                    i[0] += 0
                    i[1] += 3
                elif i[2] == 2:
                    i[0] += 3
                    i[1] += 3
                elif i[2] == 3:
                    i[0] += -3
                    i[1] += 3
                elif i[2] == 4:
                    i[0] += 3
                    i[1] += -3
                elif i[2] == 5:
                    i[0] += -3
                    i[1] += -3
                elif i[2] == 6:
                    i[0] += 3
                    i[1] += 0
                elif i[2] == 7:
                    i[0] += -3
                    i[1] += 0
                if i[0] <= 0 or i[0] >= main_game.WIDTH or i[1] <= 0 or i[1] >= main_game.HEIGHT:
                    self.debris.remove(i)
            self.check()
            if randint(0, 80) == 0:
                self.add_enemy()
            main_game.app.clock['text'] = "You have " + str(self.shots_left) + " shots left and " + str(self.score) + " points."

    def draw(self):
        main_game.app.canvas.delete(ALL)

        main_game.app.canvas.create_rectangle((main_game.WIDTH / 11) * 5, main_game.HEIGHT, (main_game.WIDTH / 11) * 6, main_game.HEIGHT - (( main_game.HEIGHT / 4)))

        for i in self.shots:
            main_game.app.canvas.create_rectangle(i[0], i[1], i[0] + 10, i[1] + 5)

        for i in self.enemys:
            main_game.app.canvas.create_oval(i[0], i[1], i[0] + 25, i[1] + 25, fill = "black")

        for i in self.debris:
            main_game.app.canvas.create_oval(i[0], i[1], i[0] + 17, i[1] + 17)

    def add_enemy(self):
        if randint(0, 1) == 0:
            self.enemys.append([-25, randint(25, 125), 0])
        else:
            self.enemys.append([main_game.WIDTH + 25, randint(25, 125), 1])

    def check(self):
        for i in self.enemys:
            self.dead = False
            for a in self.shots:
                if a[0] >= i[0] and a[0] <= i[0] + 17 and a[1] >= i[1] and a[1] <= i[1] + 17:
                    if self.dead:
                        pass
                    else:
                        self.enemys.remove(i)
                        self.shots.remove(a)
                        self.explode(i[0], i[1])
                        self.score += 2
                        self.dead = True

        for i in self.enemys:
            self.dead = False
            for a in self.debris:
                    if a[0] >= i[0] and a[0] <= i[0] + 25 and a[1] >= i[1] and a[1] <= i[1] + 25:
                        if self.dead:
                            pass
                        else:
                            self.enemys.remove(i)
                            self.explode(i[0], i[1])
                            self.debris.remove(a)
                            self.score += 2
                            self.dead = True

        for i in self.enemys:
            if i[2] == 0 and i[0] >= main_game.WIDTH:
                self.enemys.remove(i)
            elif i[2] == 1 and i[0] <= 0:
                self.enemys.remove(i)

        if self.shots_left == 0 and self.shots == [] and self.debris == []:
            self.end()

    def shoot(self):
        if self.shots_left == 0:
            pass
        else:
            self.shots.append([(main_game.WIDTH / 11) * 5.5, main_game.HEIGHT - (( main_game.HEIGHT / 4))])
            self.shots_left -= 1

    def laser(self):
        self.temp_no = 0
        for i in range(0, 50):
            self.shots.append([(main_game.WIDTH / 11) * 5.5, main_game.HEIGHT - (( main_game.HEIGHT / 4)) - self.temp_no])
            self.temp_no += 10

    def explode(self, x, y):
        self.debris.append([x, y, 0])
        self.debris.append([x, y, 1])
        self.debris.append([x, y, 2])
        self.debris.append([x, y, 3])
        self.debris.append([x, y, 4])
        self.debris.append([x, y, 5])
        self.debris.append([x, y, 6])
        self.debris.append([x, y, 7])

    def end(self):
        self.RUN = False
        main_game.app.point += self.score
        main_game.app.old_point = self.score
        main_game.app.time += 60
        main_game.app.run_once = True
        main_game.game = "bus"

app = chainreaction()

