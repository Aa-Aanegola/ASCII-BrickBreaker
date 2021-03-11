from .defs import *

class Powerup:
    def __init__(self, height, width, velocity, position):
        self.duration = POWERUP_DURATION
        self.start = int(time.time())
        self.type = BASE_POWERUP
        self.height = height
        self.width = width
        self.velocity = velocity
        self.position = position
        self.character = 'X'
        
    def return_type(self):
        return self.type
    
    def apply_effect(self):
        self.start = int(time.time())
        return 
    
    def remove_effect(self):
        return
    
    def expired(self):
        if int(time.time() - self.start) >= self.duration:
            return True
        return False
    
    def move(self, paddle):
        y, x = self.position
        vel_y, vel_x = self.velocity 
        new_y = y + vel_y
        new_x = x + vel_x
        if new_y+1 > self.height:
            new_y = self.height - 1
        if new_x < 1:
            new_x = 1
            vel_x *= -1
        if new_x > self.width:
            new_x = self.width 
            vel_x *= -1
        self.position = (new_y, new_x)
        self.velocity = (vel_y, vel_x)
        if y+1 == self.height:
            if paddle.position - PADDLE_LENGTH <= x <= paddle.position + PADDLE_LENGTH:
                return ADD_POWERUP
            return REMOVE_POWERUP
        return KEEP_POWERUP
    
    def draw(self):
        Print([MOVE_CURSOR % self.position, self.character])
        Print([MOVE_CURSOR % (self.height+5, 1), RESET])
    
    def undraw(self, color):
        Print([MOVE_CURSOR % self.position, color + ' '])
        Print([MOVE_CURSOR % (self.height+5, 1)])    
    
class ShrinkPaddle(Powerup):
    def __init__(self, height, width, velocity, position):
        super().__init__(height, width, velocity, position)
        self.type = SHRINK_PADDLE
        self.character = SHRINK_PADDLE_CHARACTER
        
    def apply_effect(self, ball, paddle, player):
        self.start = int(time.time())
        paddle.shrink()
        
    def remove_effect(self, ball, paddle, player):
        paddle.reset_length() 
        
class GrowPaddle(Powerup):
    def __init__(self, height, width, velocity, position):
        super().__init__(height, width, velocity, position)
        self.type = GROW_PADDLE
        self.character = GROW_PADDLE_CHARACTER
        
    def apply_effect(self, ball, paddle, player):
        paddle.grow()
    
    def remove_effect(self, ball, paddle, player):
        paddle.reset_length()
                
class FastBall(Powerup):
    def __init__(self, height, width, velocity, position):
        super().__init__(height, width, velocity, position)
        self.type = FAST_BALL
        self.character = FAST_BALL_CHARACTER
        
    def apply_effect(self, ball, paddle, player):
        ball.multiplier = 2
    
    def remove_effect(self, ball, paddle, player):
        ball.multiplier = 1
        
class PaddleGrab(Powerup):
    def __init__(self, height, width, velocity, position):
        super().__init__(height, width, velocity, position)
        self.type = PADDLE_GRAB
        self.character = PADDLE_GRAB_CHARACTER
        
    def apply_effect(self, ball, paddle, player):
        paddle.grab = True
    
    def remove_effect(self, ball, paddle, player):
        paddle.grab = False
        
class ThruBall(Powerup):
    def __init__(self, height, width, velocity, position):
        super().__init__(height, width, velocity, position)
        self.type = THRU_BALL
        self.character = THRU_BALL_CHARACTER
        
    def apply_effect(self, ball, paddle, player):
        ball.thru = True
    
    def remove_effect(self, ball, paddle, player):
        ball.thru = False
        
class LaserPaddle(Powerup):
    def __init__(self, height, width, velocity, position):
        super().__init__(height, width, velocity, position)
        self.type = LASER_PADDLE
        self.character = LASER_PADDLE_CHARACTER
        
    def apply_effect(self, ball, paddle, player):
        paddle.laser = True
    
    def remove_effect(self, ball, paddle, player):
        paddle.laser = False 
        Print([MOVE_CURSOR % (paddle.height-1, 1), ' '*45])

class FireBall(Powerup):
    def __init__(self, height, width, velocity, position):
        super().__init__(height, width, velocity, position)
        self.type = FIRE_BALL
        self.character = FIRE_BALL_CHARACTER
    
    def apply_effect(self, ball, paddle, player):
        ball.fire = True
    
    def remove_effect(self, ball, paddle, player):
        ball.fire = False

class Bomb(Powerup):
    def __init(self, height, width, velocit, position):
        super().__init__()
        self.type = UFO_BOMB
        self.character = 'O'
    
    def apply_effect(self, ball, paddle, player):
        player.lives -= 1
    
    def remove_effect(self, ball, paddle, player):
        return