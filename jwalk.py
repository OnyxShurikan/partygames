__author__ = 'Cole'

#Copyright Cole Gosney 2014
#The 'Jwalking' game

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from random import randint

import main_game

class jwalk:
    def __init__(self):
        self.players = []
        self.player = []
        self.vel = [0, 0]
        self.score = 0
        self.lane_one_cars = []
        self.lane_two_cars = []
        self.lane_three_cars = []
        self.lane_four_cars = []
        self.RUN = False
    
    def start(self):
        self.players = []
        for i in range(1, 25):
            self.temp_pos = [(main_game.WIDTH / 8) / 2, (main_game.HEIGHT / 25) * i]
            self.players.append(self.temp_pos)
        self.player = 1
        self.vel = [0, 0]
        self.score = 0
        self.lane_one_cars = []
        self.lane_two_cars = []
        self.lane_three_cars = []
        self.lane_four_cars = []
        self.RUN = True
        
    def update(self):
        if self.RUN:
            self.car_check()
            self.draw()
            self.player_check()
            self.temp_count = 0
            for i in self.players:
                self.temp_count += 1
                if self.temp_count == self.player:
                    i[0] += self.vel[0]
                    i[1] += self.vel[1]
            self.add_car()
            main_game.app.clock['text'] = str(self.score) + " people out of 25 has made it to the other side!"
        
    def draw(self):
        main_game.app.canvas.delete(ALL)
        
        for i in range(1, 8):
            if i == 4:
                pass
            else:
                main_game.app.canvas.create_line((main_game.WIDTH / 8) * i, 1, (main_game.WIDTH / 8) * i, main_game.HEIGHT - 1)
                
        for i in self.players:
            main_game.app.canvas.create_oval(i[0], i[1], i[0] + 25, i[1] + 25, fill = "black")

        for i in self.lane_one_cars:
            main_game.app.canvas.create_rectangle(i[0], i[1], i[0] + (main_game.WIDTH / 8) - 20, i[1] - 50)
        for i in self.lane_two_cars:
            main_game.app.canvas.create_rectangle(i[0], i[1], i[0] + (main_game.WIDTH / 8) - 20, i[1] - 50)
        for i in self.lane_three_cars:
            main_game.app.canvas.create_rectangle(i[0], i[1], i[0] + (main_game.WIDTH / 8) - 20, i[1] - 50)
        for i in self.lane_four_cars:
            main_game.app.canvas.create_rectangle(i[0], i[1], i[0] + (main_game.WIDTH / 8) - 20, i[1] - 50)

    def add_car(self):
        if len(self.lane_one_cars) > 5:
            pass
        else:
            if randint(0, 60) == 0:
                self.lane_one_cars.append([((main_game.WIDTH / 8) * 1) + 10, -1, randint(3, 4)])
        if len(self.lane_two_cars) > 5:
            pass
        else:
            if randint(0, 60) == 0:
                self.lane_two_cars.append([((main_game.WIDTH / 8) * 2) + 10, -1, randint(3, 4)])
        if len(self.lane_three_cars) > 5:
            pass
        else:
            if randint(0, 60) == 0:
                self.lane_three_cars.append([((main_game.WIDTH / 8) * 5) + 10, -1, randint(3, 4)])
        if len(self.lane_four_cars) > 5:
            pass
        else:
            if randint(0, 60) == 0:
                self.lane_four_cars.append([((main_game.WIDTH / 8) * 6) + 10, -1, randint(3, 4)])

    def car_check(self):
        for i in self.lane_one_cars:
                if i[1] - 50 >= main_game.HEIGHT:
                    self.lane_one_cars.remove(i)
                else:
                    i[1] += i[2]
        for i in self.lane_two_cars:
                if i[1] - 50 >= main_game.HEIGHT:
                    self.lane_two_cars.remove(i)
                else:
                    i[1] += i[2]

        for i in self.lane_three_cars:
                if i[1] - 50 >= main_game.HEIGHT:
                    self.lane_three_cars.remove(i)
                else:
                    i[1] += i[2]
        for i in self.lane_four_cars:
                if i[1] - 50 >= main_game.HEIGHT:
                    self.lane_four_cars.remove(i)
                else:
                    i[1] += i[2]

    def player_check(self):
        self.temp_count = 0
        for i in self.players:
            self.temp_count += 1
            if self.temp_count == self.player:
                if i[0] >= (main_game.WIDTH / 8) * 7 + (0.25 * (main_game.WIDTH / 8)):
                    self.change_player(True)
                elif i[0 ]<= 0:
                    i[0] = 1
                elif i[1] <= 0:
                    i[1] = 1
                elif i[1] + 25 >= main_game.HEIGHT:
                    i[1] = main_game.HEIGHT -26
                else:

                    for a in self.lane_one_cars:
                        if i[0] + 12.5 >= a[0] and i[0] <= a[0] + (main_game.WIDTH / 8) - 20:
                            if i[1] <= a[1] and i[1] + 12.5 >= a[1] - 50:
                                self.change_player(False)
                    for a in self.lane_two_cars:
                        if i[0] + 12.5 >= a[0] and i[0] <= a[0] + (main_game.WIDTH / 8) - 20:
                            if i[1] <= a[1] and i[1] + 12.5 >= a[1] - 50:
                                self.change_player(False)
                    for a in self.lane_three_cars:
                        if i[0] + 12.5 >= a[0] and i[0] <= a[0] + (main_game.WIDTH / 8) - 20:
                            if i[1] <= a[1] and i[1] + 12.5 >= a[1] - 50:
                                self.change_player(False)
                    for a in self.lane_four_cars:
                        if i[0] + 12.5 >= a[0] and i[0] <= a[0] + (main_game.WIDTH / 8) - 20:
                            if i[1] <= a[1] and i[1] + 12.5 >= a[1] - 50:
                                self.change_player(False)

    def change_player(self, line):
        self.player += 1
        if self.player > 24:
            self.end()
        if line:
            self.score += 1

    def end(self):
        self.RUN = False
        main_game.app.point += self.score * 5
        main_game.app.old_point = self.score * 5
        main_game.app.time += 60
        main_game.app.run_once = True
        main_game.game = "bus"

app = jwalk()
