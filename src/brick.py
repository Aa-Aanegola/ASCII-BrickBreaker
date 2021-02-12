from .defs import *

class Brick:
    """
        colors: list of all possible colors of bricks
        count: count of all active (strength != 0) bricks present
    """
    colors = [RESET, CYAN, GREEN, MAGENTA, WHITE]
    count = 0
    def __init__(self, strength):
        self.strength = min(strength, 4)
        self.color = Brick.colors[self.strength]
        if self.strength != 4 and self.strength != 0:
            Brick.count += 1
        
    def notEmpty(self):
        if self.strength:
            return True 
        return False
    
    def damage(self, y, x):
        if self.strength == 4 or self.strength == 0:
            return NO_EFFECT
        self.strength -= 1
        self.color = Brick.colors[self.strength]
        
        Print([MOVE_CURSOR % (y+1, BRICK_LENGTH*x+1),
               self.color + ' ' * BRICK_LENGTH,
               RESET])
        
        if self.strength == 0:
            Brick.count -= 1
            return DESTROYED
        
        return DAMAGED