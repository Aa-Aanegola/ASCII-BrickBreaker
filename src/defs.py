import colorama
import random
import time
import copy

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
# Number of levels
NUM_LEVELS = 3

# Length of bricks in terms of ascii characters
BRICK_LENGTH = 3

# Number of rows between last brick row and paddle
EMPTY_ROWS = 20

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
MAX_LIVES = 3
HIT_SCORE = 1
DESTROY_SCORE = 5
UFO_SCORE = 100
NO_EFFECT = "Jar Jar Binks"
DESTROYED = "Alderaan"
DAMAGED = "Anakin Skywalker"
UFO_DESTROYED = "Death Star"

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
LASER_PADDLE_CHARACTER = 'L'
FIRE_BALL_CHARACTER = 'E'

BASE_POWERUP = "to be or not to be"
SHRINK_PADDLE = "shrinky paddle"
GROW_PADDLE = "paddle go brrr"
FAST_BALL = "speedy bollocks"
PADDLE_GRAB = "A Jedi craves not attachment"
THRU_BALL = "Not even Beskar..."
LASER_PADDLE = "E-WEB Heavy Repeating Blaster"
FIRE_BALL = "Who needs an imperial star destroyer?"

POWERUP_LIST = [SHRINK_PADDLE, GROW_PADDLE, FAST_BALL, PADDLE_GRAB, THRU_BALL, LASER_PADDLE, FIRE_BALL]

# Print with separator and end defined to be ''
Print = lambda content: print(*content, sep='', end='', flush=True)

# Time after which the level moves down a notch
BRICK_FALL_TIME = 30

# Time interval between two laser beams 
LASER_INTERVAL = 2

# UFO defs
UFO_HEALTH = 10
UFO_ROW_DELAY = 20
UFO_BOMB_DELAY = 3