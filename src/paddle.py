from .defs import *

class Paddle:
    # Initializes position, length and color
    def __init__(self, position, height, bound):
        self.position = position
        self.bound = bound
        self.length = PADDLE_LENGTH
        self.color = PADDLE_COLOR
        self.height = height
        self.grab = False
        
    # Sets the length of the paddle
    def shrink(self):
        self.length = MIN_PADDLE_LENGTH
    
    def grow(self):
        if self.position - MAX_PADDLE_LENGTH < 0:
            self.position += 1
        if self.position + MAX_PADDLE_LENGTH > self.bound:
            self.position -= 1
        
        self.length = MAX_PADDLE_LENGTH
    
    def reset_length(self):
        if self.position - PADDLE_LENGTH < 0:
            self.position += 1
        if self.position + PADDLE_LENGTH > self.bound:
            self.position -= 1
            
        self.length = PADDLE_LENGTH
    
    def draw(self):
        Print(MOVE_CURSOR % (self.height, 0))
        Print([' '*(self.position - self.length),
              self.color + ' '*(self.length*2+1),
              RESET,
              ' '*(self.bound - self.length - self.position+2)
        ])
        Print(MOVE_CURSOR % (self.height+3, 0))
    
    def move(self, direction):
        if self.position - self.length + direction < 0:
            return False
        if self.position + self.length + direction > self.bound:
            return False 
        self.position += direction
        return True

    def reset_position(self):
        self.position = self.bound//2 + 1
        self.reset_length()

    def get_data(self):
        return (self.position, self.length)
        