from .defs import *

class Powerup:
    def __init__(self, bound, position):
        self.duration = POWERUP_DURATION
        self.start = int(time.time())
        self.type = BASE_POWERUP
        self.bound = bound
        self.position = position
        self.character = 'X'
        
    def return_type(self):
        return self.type
    
    def apply_effect(self):
        self.start = int(time.time())
        return 
    
    def remove_affect(self):
        return
    
    def expired(self):
        if int(time.time() - self.start) >= self.duration:
            return True
        return False
    
    def move(self, paddle):
        y, x = self.position
        self.position = (y+1, x)
        
        if y+1 == self.bound:
            if paddle.position - PADDLE_LENGTH <= x <= paddle.position + PADDLE_LENGTH:
                return ADD_POWERUP
            return REMOVE_POWERUP
        return KEEP_POWERUP
    
    def draw(self):
        Print([MOVE_CURSOR % self.position, self.character])
        Print([MOVE_CURSOR % (self.bound+5, 1), RESET])
    
    def undraw(self, color):
        Print([MOVE_CURSOR % self.position, color + ' '])
        Print([MOVE_CURSOR % (self.bound+5, 1)])    
    
class ShrinkPaddle(Powerup):
    def __init__(self, bound, position):
        super().__init__(bound, position)
        self.type = SHRINK_PADDLE
        self.character = SHRINK_PADDLE_CHARACTER
        
    def apply_effect(self, ball, paddle):
        self.start = int(time.time())
        paddle.shrink()
        
    def remove_effect(self, ball, paddle):
        paddle.reset_length() 
        
class GrowPaddle(Powerup):
    def __init__(self, bound, position):
        super().__init__(bound, position)
        self.type = GROW_PADDLE
        self.character = GROW_PADDLE_CHARACTER
        
    def apply_effect(self, ball, paddle):
        paddle.grow()
    
    def remove_effect(self, ball, paddle):
        paddle.reset_length()
                
class FastBall(Powerup):
    def __init__(self, bound, position):
        super().__init__(bound, position)
        self.type = FAST_BALL
        self.character = FAST_BALL_CHARACTER
        
    def apply_effect(self, ball, paddle):
        ball.multiplier = 2
    
    def remove_effect(self, ball, paddle):
        ball.multiplier = 1
        
class PaddleGrab(Powerup):
    def __init__(self, bound, position):
        super().__init__(bound, position)
        self.type = PADDLE_GRAB
        self.character = PADDLE_GRAB_CHARACTER
        
    def apply_effect(self, ball, paddle):
        paddle.grab = True
    
    def remove_effect(self, ball, paddle):
        paddle.grab = False