__author__ = 'Cole'

#Copyright Cole Gosney 2014
#The 'run' game

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from random import randint                              #Imports needed modules

import main_game

class run:                                              #Running game
    def __init__(self):
        self.checks = range(-13, 13)                    #Sets the collision variable
        self.pos = [400, 400, 425, 425]
        self.vel = [0, 0]
        self.enemy = []                                 #Sets player and enemy positions for start
        self.time = 0                                   #Sets time to 0
        self.RUN = False                                #Sets the timer variable to False
        
    def start(self):
        self.RUN = True                                 #Sets the timer variable to True
        self.pos = [400, 400, 425, 425]
        self.vel = [0, 0]
        self.time = 0
        self.enemey = []                                #Resets all variable between games
        
    def update(self):
        if self.RUN:
            self.time += 1                              #Adds 1/60 of a second to the time 
            self.draw()                                 #Calls the draw handler
            self.collision()                            #Calls the collision handler
            if self.pos[0] + 12.5 <= 0:
                self.pos[0] = main_game.WIDTH - 12.5
            elif self.pos[0] + 12.5 >= main_game.WIDTH:
                self.pos[0] = 1
            elif self.pos[1] + 12.5 <= 0:
                self.pos[1] = main_game.HEIGHT - 12.5
            elif self.pos[1] +12.5 >= main_game.HEIGHT:
                self.pos[1] = 1                         #Warps the player around the screen if they go outsude the screen limits
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]
            self.pos[2] = self.pos[0] + 25
            self.pos[3] = self.pos[1] + 25              #Updates the positions of the player by the velocity
            self.x = randint(0, 40)
            if self.x == 0:
                self.add_enemy()                        #Gives a 1 in 40 chance to spawn an enemy 
            self.ai()                                   #Moves the enemy according to the ai handler

            main_game.app.clock['text'] = "Time: " + str((self.time / 60) // 1)   #Sets the mini-game timer to show in place of the bus timer
            
    def add_enemy(self):
        self.temp_pos = [randint(0, main_game.WIDTH), randint(0, main_game.HEIGHT)] #Generates a random position inside the screen limits
        self.enemy.append(self.temp_pos)                #Adds an enemy to the enemy list

    def ai(self):
        for i in self.enemy:                            #Loops through the enemys in the enemy list, calling each 'i'
            self.x = randint(0, 60)                     #Gives a 1 in 60 change the enemy will move in the oposit direction
            if self.pos[1] + 12.5 > i[1] + 12.5:        #Sees if the enemys y is smaller than the players y BY CENTRE
                if self.x ==0:
                    i[1] -=4                            #The 1 in 60 chance
                else:
                    i[1] += 2                           #Moves the enemys y closer to the players y by one movement
            elif self.pos[1] + 12.5 < i[1] + 12.5:      #Sees if the enemys y is bigger than the players y BY CENTRE
                if self.x ==0:
                    i[1] +=4                            #The 1 in 60 chance
                else:
                    i[1] -= 2                           #Moves the enemys y closer to the players y by one movement
            elif self.pos[1] + 12.5 == i[1] +12.5:      #Sees if the enemys y is on the same level to the players y BY CENTRE
                i[1] = i[1]                             #Keeps the enemy at the same y level
                
            if self.pos[0] + 12.5 > i[0] + 12.5:        #Sees if the enemys x is smaller than the players x BY CENTRE
                if self.x ==0:
                    i[0] -=4                            #The 1 in 60 chance
                else:
                    i[0] += 2                           #Moves the enemys x closer to the players x by one movement
            elif self.pos[0] + 12.5 < i[0] + 12.5:      #Sees if the enemys x is bigger than the players x BY CENTRE
                if self.x ==0:
                    i[0] +=4                            #The 1 in 60 chance
                else:
                    i[0] -= 2                           #Moves the enemys x closer to the players x by one movement
            elif self.pos[0] + 12.5 == i[0] +12.5:      #Sees if the enemys x is on the same level to the players x BY CENTRE
                i[0] = i[0]                             #Keeps the enemy at the same x level

    def collision(self):
        for i in self.enemy:                            #Loops through the enemys in the enemy list, calling each 'i'
            if int(self.pos[0]) - int(i[0]) in self.checks and int(self.pos[1]) - int(i[1]) in self.checks: #Sees if the x - x and y - y of player and enemy are within the range paramiters of self.checks
                self.end()                              #Calls self.end() to end the game
                
    
    def draw(self):
        main_game.app.canvas.delete(ALL)                #Clears the canvas
        
        main_game.app.canvas.create_oval(self.pos[0], self.pos[1], self.pos[2], self.pos[3], fill = "black")  #Draws the player with a diamiter of 25 pixels
        for i in self.enemy:                            #Loops through the enemys in the enemy list, calling each 'i'
            main_game.app.canvas.create_oval(i[0], i[1], i[0] + 25, i[1] + 25, fill = "red")  #Draws the enemy with a diamiter of 25 pixels

    def end(self):
        global game                                     #Sets game as a global variable
        self.RUN = False                                #Sets the timer variable to False
        self.enemy = []                                 #Deletes all enemys
        main_game.app.point += ((self.time / 60) * 2) // 1
        main_game.app.old_point = ((self.time / 60) * 2) // 1   #Updates the points for the main game - bus
        main_game.app.time += 60                        #Adds a second onto the main timer - bus
        main_game.app.run_once = True                   #Resets the burn-out variable
        main_game.game = "bus"                          #Puts the game back to main - bus

app = run()
