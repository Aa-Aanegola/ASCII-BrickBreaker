import colorama
from src.grid import Grid
from src.input import *
import os

# We need to clear the screen for cursor position
os.system('clear')
os.system("stty -echo")
colorama.init()

# Set up our game display
arena = Grid('./extra/level.txt')
arena.initialise_display()

# Defining our input function
getch = Get()

while True:
    # Input 
    keystroke = input_to(getch)
    
    # If it is a quit condition, quit, otherwise take action
    if keystroke != None and arena.use_keystroke(keystroke) == False:
            break
        
    if arena.update() == False:
            break

arena.display_message()
os.system("stty echo")