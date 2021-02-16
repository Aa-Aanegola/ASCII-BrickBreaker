import colorama
import random
import time

# Colorama colors
RED = colorama.Back.RED 
RESET = colorama.Back.RESET
CYAN = colorama.Back.CYAN
GREEN = colorama.Back.GREEN
MAGENTA = colorama.Back.MAGENTA
WHITE = colorama.Back.WHITE

# Foreground color
YELLOW = colorama.Fore.YELLOW

# Changing cursor position
MOVE_CURSOR = "\033[%d;%dH"

"""
    Default values for some parameters
"""
# Length of bricks in terms of ascii characters
BRICK_LENGTH = 3

# Number of rows between last brick row and paddle
EMPTY_ROWS = 21

# Paddle span from centre to end
PADDLE_LENGTH = 3
MIN_PADDLE_LENGTH = 2
MAX_PADDLE_LENGTH = 4

# Paddle color
PADDLE_COLOR = WHITE
PADDLE_SPEED = 1

# Ball color
BALL_COLOR = YELLOW

# Directions with their respective effects
LEFT = -1 * PADDLE_SPEED
RIGHT = 1 * PADDLE_SPEED
UP = -1
DOWN = 1

# Return values for collision detection
LFACE = "kablamo"
RFACE = "watch your face!"
UFACE = "I walked into a pole"
DFACE = "gravity says hi"
EXITED = "ggwp"

# Player values
MAX_LIVES = 5
HIT_SCORE = 1
DESTROY_SCORE = 5
NO_EFFECT = "Jar Jar Binks"
DESTROYED = "Death Star"
DAMAGED = "Anakin Skywalker"


# Powerup related definitions 
POWERUP_DURATION = 10
POWERUP_PROBABILITY = 1

ADD_POWERUP = "Unlimited Power!"
REMOVE_POWERUP = "NOOOOOO!!"
KEEP_POWERUP = "Bad Juju"

SHRINK_PADDLE_CHARACTER = 'S'
GROW_PADDLE_CHARACTER = 'G'
FAST_BALL_CHARACTER = 'F'
PADDLE_GRAB_CHARACTER = 'P'
THRU_BALL_CHARACTER = 'T'

BASE_POWERUP = "to be or not to be"
SHRINK_PADDLE = "shrinky paddle"
GROW_PADDLE = "paddle go brrr"
FAST_BALL = "speedy bollocks"
PADDLE_GRAB = "A Jedi craves not attachment"
THRU_BALL = "Not even Beskar..."


POWERUP_LIST = [SHRINK_PADDLE, GROW_PADDLE, FAST_BALL, PADDLE_GRAB, THRU_BALL]

# Print with separator and end defined to be ''
Print = lambda content: print(*content, sep='', end='', flush=True)