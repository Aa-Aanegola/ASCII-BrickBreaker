from .defs import *

class Ball:
    def __init__(self, y, x, width, height):
        self.color = BALL_COLOR
        
        # Position is 1 indexed due to cursor behavior
        self.y = y
        self.x = x
        
        self.multiplier = 1
        
        # Width and height of playable area
        self.width = width
        self.height = height
        
        self.velocity = (-1, self.x - 1 - self.width//2)#random.randint(-PADDLE_LENGTH, PADDLE_LENGTH))
    
        self.thru = False
    
    # Return the current position of the ball
    def get_position(self):
        return (self.y, self.x)
    
    def set_position(self, position):
        y, x = position
        self.y = y
        self.x = x
    
    def get_velocity(self):
        return self.velocity
    
    def set_velocity(self, velocity):
        vel_y, vel_x = velocity
        vel_y /= abs(vel_y)
        vel_y *= self.multiplier
        self.velocity = (vel_y, vel_x)
    
    # Draw the ball on the display
    def draw(self):
        Print([MOVE_CURSOR % self.get_position(), self.color + 'o', RESET])
        
    def undraw(self):
        Print([MOVE_CURSOR % self.get_position(), RESET, ' '])
        
    def reset_position(self):
        self.y = self.height
        self.x = self.width//2 + 2 + random.randint(-PADDLE_LENGTH, PADDLE_LENGTH)
        self.velocity = (-1*self.multiplier, self.x - 2 - self.width//2)
        
    def move(self, direction):
        if self.x + direction < 1 or self.x + direction > self.width:
            return
        self.x += direction