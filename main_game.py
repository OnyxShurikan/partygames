__author__ = 'Cole'

#Copyright Cole Gosney 2014
#Holds the 'core' of the game

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from time import sleep
from random import randint                              #Imports needed modules

import zergrush
import jwalk
import run
import chain_reaction
import littlebird

WIDTH = 800
HEIGHT = 600                                            #Sets CHANGABLE variables

game = "bus"
games = {1:"bus", 2:"run", 3:"jwalk", 4:"zergrush", 5:"chainreaction", 6:"littlebird"}     #Sets UNCHANGABLE variables

class Game:
    def __init__(self):
        self.root = Tk() 				#Sets the Tkinter root
        self.RUN = False 				#Sets the timer loop variable to false

        self.frame = Frame(self.root, bg = "white")
        self.frame.bind("<Key>", self.keydown)
        self.frame.bind("<KeyRelease>", self.keyup)
        self.frame.pack()				#Creates a frame, binds the keyboard to it and then packs it

        self.canvas = Canvas(self.frame, bg = "white", width = WIDTH, height = HEIGHT)
        self.canvas.bind("<Button-1>", self.mouseclick)
        self.canvas.pack()				#Creates a canvas and then packs it

        self.clock = Label(self.frame, bg = "white", fg = "black")
        self.clock.pack()				#Creates a label that holds time data
        
        self.points = Label(self.frame, bg = "white", fg = "black")
        self.points.pack()				#Creates a label that holds score data

        self.dev_console = Entry(self.root)
        self.dev_console.pack()
        
        self.button = Button(self.frame, bg = "white", fg = "black", text = "Start", command = self.start)
        self.button.pack()				#Creates a button that starts the game by calling self.start()
   
        self.edc = Button(self.frame, bg = "white", fg = "black", text = "Submit Dev Command", command = self.dev_commands)
        self.edc.pack()

        self.frame.focus_set()				#Sets the focus to the frame for keyboard input

    def run(self):
        if self.RUN is True:				#Checks if the timer loop is true to run the timer
            self.update()				#Updates the current game, score, timer and canvas by calling self.update()
            self.root.after(10, self.run)		#Calls self.run() again to create a loop

    def start(self):
        self.point = 0
        self.old_point = 0
        self.time = 0
        self.round = 0
        self.RUN = True
        self.run_once = True				#Sets the points to 0, old_points to 0, time to 0, round to 0, make the timer variable True and sets the burn out to True

        self.rone = [WIDTH / 4, 0, WIDTH / 4, 800]
        self.rtwo = [WIDTH - (WIDTH / 4), 0, WIDTH - (WIDTH / 4), 800]	#Sets the road coordinates

        self.vel = [0.5, 0]				#Sets the road movement velocity

        self.button['text'] = "Quit"
        self.button['command'] = self.end		#Changes the 'text' tag on the button to 'quit' and the 'command' tag to run self.end()
        
        self.run()					#Starts the clock

    def update(self):
        global game					#Sets 'game' as a global variable
        if game == "run":
            if self.run_once is True:
                run.app.start()
                self.run_once = False                   #This loop calls the minigame's .start() to reset variables in said minigame, and only runs it once due to the use of a burn-out variable
            run.app.update()
        elif game == "jwalk":
            if self.run_once is True:
                jwalk.app.start()
                self.run_once = False
            jwalk.app.update()
        elif game == "zergrush":
            if self.run_once is True:
                zergrush.app.start()
                self.run_once = False
            zergrush.app.update()
        elif game == "chainreaction":
            if self.run_once is True:
                chain_reaction.app.start()
                self.run_once = False
            chain_reaction.app.update()
        elif game == "littlebird":
            if self.run_once is True:
                littlebird.app.start()
                self.run_once = False
            littlebird.app.update()
        elif game == "bus":				#This if loop checks what game is selected and runs the update for it
            self.clock['text'] = "Time:" + str((self.time / 60) // 1)
            self.points['text'] = "Points Overall: " + str(self.point) + " Points scored last round: " + str(self.old_point) + " You have played " +str(self.round) + " rounds."    #Sets the 'clock' and 'text' lables to visable

            if int((self.time / 60) // 1) % 5 == 0 and ((self.time / 60) //1) not in [0]:
                self.round += 1
                temp = randint(2, 4)
                game = games[temp]
                self.points['text'] = games[temp] + " is comming up!"   #Checks if the time in seconds is divisable by five, and chooses a random game to play

            self.draw()                                 #Calls the draw handler
        
            self.time += 1                              #Adds on 1/60 of a second to time
        
            self.rone[0] += self.vel[0]
            self.rone[1] += self.vel[1]
            self.rone[2] += self.vel[0]
            self.rone[3] += self.vel[1]                 #Moves RoadOne based on velocity

            self.rtwo[0] += self.vel[0]
            self.rtwo[1] += self.vel[1]
            self.rtwo[2] += self.vel[0]
            self.rtwo[3] += self.vel[1]                 #Moves RoadTwo based on velocity

            if self.rone[0] >= WIDTH / 2.9090909 or self.rtwo[0] <= WIDTH - (WIDTH / 2.9090909):
                self.points['text'] = "Game Over! You got " + str(self.point) + " points!"
                self.RUN = False                        #Checks if you have gone over the road and ends game if you have

    def keydown(self, key):
        if game == "run":                               #Checks for a keydown event
            if key.char == "w":
                run.app.vel[1] = -2
            elif key.char == "s":
                run.app.vel[1] = 2

            elif key.char == "a":
                run.app.vel[0] = -2
            elif key.char == "d":
                run.app.vel[0] = 2                      #Changes your characters movement velocity
        elif game == "jwalk":
            if key.char == "w":
                jwalk.app.vel[1] = -2
            elif key.char == "s":
                jwalk.app.vel[1] = 2
            elif key.char == "a":
                jwalk.app.vel[0] = -2
            elif key.char == "d":
                jwalk.app.vel[0] = 2                    #Changes your character movement velocity
        elif game == "zergrush":
            pass                                        #Keyboard not used for this game
        elif game == "chainreaction":
            if key.char == "w":
                if chain_reaction.app.shot_type == "laser":
                    chain_reaction.app.laser()
                elif chain_reaction.app.shot_type == "shot":
                    chain_reaction.app.shoot()                  #Fires a shot
        elif game == "littlebird":
            if key.char == "w":
                if not littlebird.app.flying:
                    littlebird.app.fly()
        elif game == "bus":
            if key.char == "a":
                self.vel[0] = -1                        #Moves the bus
            

    def keyup(self, key):
        if game == "run":                               #Checks for a keyup event
            if key.char == "w":
                run.app.vel[1] = 0
            elif key.char == "s":
                run.app.vel[1] = 0
            elif key.char == "a":
                run.app.vel[0] = 0
            elif key.char == "d":
                run.app.vel[0] = 0                      #Resets your characters movement velocity
        elif game == "jwalk":
            if key.char == "w":
                jwalk.app.vel[1] = 0
            elif key.char == "s":
                jwalk.app.vel[1] = 0
            elif key.char == "a":
                jwalk.app.vel[0] = 0
            elif key.char == "d":
                jwalk.app.vel[0] = 0                    #Resets your characters movement velocity
        elif game == "zergrush":
            pass                                        #Keyboard not used for this game
        elif game == "chainreaction":
            pass                                        #Keyup not used for this game
        elif game == "littlebird":
            pass
        elif game == "bus":
            if key.char == "a":
                self.vel[0] = 1.25                      #Resets the bus' movement velocity

    def mouseclick(self, pos):
        if game == "run":                               #Checks for a mouseclick even
            pass                                        #Mouse not used for this game
        elif game == "jwalk":
            pass                                        #Mouse not used for this game
        elif game == "zergrush":
            zergrush.app.check(pos.x, pos.y)            #Checks weather it should destroy an enmey or not
        elif game == "chainreaction":
            pass                                        #Mouse not used for this game
        elif game == "bus":
            pass                                        #Mouse not used for this game

    def dev_commands(self):
        global game                                     #Calls 'game' as a global variable
        if self.dev_console.get() == "":
            self.frame.focus_set()                      #Checks if a blank command is submitted
        elif self.dev_console.get() == "reset":
            self.RUN = False
            self.time = 0
            self.point = 0
            self.old_point = 0
            self.rone[0] -= 50
            self.rone[2] -= 50
            self.rtwo[0] -= 50
            self.rtwo[2] -= 50
            game = "bus"
            self.RUN = True
            self.run()
            self.frame.focus_set()                      #Checks if reset command is submitted, refreshes RUN, sets time to 0, set both points to 0, sets the game to 'bus' and resets the roads coordiates
        elif self.dev_console.get() == "stop":
            self.RUN = False
            self.frame.focus_set()                      #Checks if stop command is submitted and sets RUN to false
        elif self.dev_console.get() == "go":
            self.RUN = False
            self.RUN = True
            self.run()
            self.frame.focus_set()                      #Checks if go command is submitted, refreshed RUN and calls the updated loop
        elif self.dev_console.get() == "ammo":
            chain_reaction.app.shots_left = 999999999999999999999999999
            self.frame.focus_set()
        elif self.dev_console.get() == "hp":
            zergrush.app.hp = 999999999999999999999999999
            self.frame.focus_set()
        elif self.dev_console.get() == "laser":
            chain_reaction.app.shot_type = "laser"
            self.frame.focus_set()
        elif self.dev_console.get() == "cross":
            for i in jwalk.app.players:
                jwalk.app.temp_count += 1
                if jwalk.app.temp_count == jwalk.app.player:
                    i[0] = WIDTH
                    i[1] = HEIGHT / 2
        else:
            if self.dev_console.get() == "bus":
                self.time += 60
                self.RUN = False
                self.RUN = True
                self.run()
                game = "bus"
                self.frame.focus_set()
            else:
                game = str(self.dev_console.get())
                self.frame.focus_set()

    def draw(self):
        self.canvas.delete(ALL)                         #Clears the canvas
        
        self.canvas.create_line(self.rone[0], self.rone[1], self.rone[2], self.rone[3])
        self.canvas.create_line(self.rtwo[0], self.rtwo[1], self.rtwo[2], self.rtwo[3]) #Draws the roads
        self.canvas.create_rectangle(WIDTH / 3.2, HEIGHT, WIDTH -(WIDTH / 3.2), HEIGHT - HEIGHT / 4)  #Draws the bus

    def end(self):
        self.RUN = False                                #Makes the timer variable false
        quit()                                          #Exits the program

app = Game()                                            #Sets the frame class to global name 'app'
app.root.mainloop()                                     #Begins the frame's mainloop
