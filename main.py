import colorama
from src.grid import Grid
from src.player import Player
from src.input import *
from src.paddle import Paddle
from src.brick import Brick
from src.ball import Ball
import os

# We need to clear the screen for cursor position
os.system('clear')
os.system("stty -echo")
colorama.init()

# Defining our input function
getch = Get()

player = Player()

for i in range(0, 3):
    # Set up level display
    os.system("clear")
    arena = Grid(f'./extra/level{i}.txt', player)
    arena.initialise_display()
    while True:
        # Input 
        keystroke = input_to(getch)

        # If it is a quit condition, quit, otherwise take action
        if keystroke != None and arena.use_keystroke(keystroke) == False:
            break

        if arena.update() == False:
            break
    
    if arena.level_complete == False:
        arena.display_message()
        break
    player.new_level(arena.ball, arena.paddle, arena.state)
    del arena
os.system("stty echo")