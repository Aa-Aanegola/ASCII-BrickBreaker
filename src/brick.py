from .defs import *

class Brick:
    """
        colors: list of all possible colors of bricks
        count: count of all active (strength != 0) bricks present
    """
    colors = [RESET, CYAN, GREEN, MAGENTA, WHITE, RED]
    count = 0
    def __init__(self, strength):
        if strength == 5:
            self.strength = 5
    
        else:
            self.strength = min(strength, 4)
    
        self.color = Brick.colors[self.strength]
        if self.strength != 4 and self.strength != 0:
            Brick.count += 1
        
    def notEmpty(self):
        if self.strength:
            return True 
        return False
    
    def damage(self, y, x, state, thru):
        if thru == False and self.strength == 4 or self.strength == 0:
            return NO_EFFECT
       
        if self.strength == 5:
            self.strength = 0
            self.explode(y, x, state, thru)
        
        broken = 1
        if self.strength == 4:
            broken = 0
        
        if thru:
            self.strength = 1
    
        
        if self.strength:
            self.strength -= 1
        
        self.color = Brick.colors[self.strength]
        
        Print([MOVE_CURSOR % (y+1, BRICK_LENGTH*x+1),
               self.color + ' ' * BRICK_LENGTH,
               RESET])
        
        if self.strength == 0:
            Brick.count -= broken
            return DESTROYED
        
        return DAMAGED
    
    def explode(self, y, x, state, thru):
        rows = len(state)
        columns = len(state[0])
        
        if y != 0:
            state[y-1][x].damage(y-1, x, state, thru)
            
            if x != 0:
                state[y-1][x-1].damage(y-1, x-1, state, thru)
                state[y][x-1].damage(y, x-1, state, thru)
                    
            if x != columns-1:
                state[y-1][x+1].damage(y-1, x+1, state, thru)
                state[y][x+1].damage(y, x+1, state, thru)

        if y != rows-1:
            state[y+1][x].damage(y+1, x, state, thru)
            
            if x != 0:
                state[y+1][x-1].damage(y+1, x-1, state, thru)
            
            if x != columns-1:
                state[y+1][x+1].damage(y+1, x+1, state, thru)