from .defs import *
from .powerups import *

class Player:
    def __init__(self, height):
        self.lives = MAX_LIVES
        self.score = 0
        self.height = height
        self.start_time = time.time()
        self.powerups = [SHRINK_PADDLE, GROW_PADDLE, FAST_BALL, PADDLE_GRAB]
        self.active = []
        self.onscreen = []
        
    def increment_score(self, destroyed):
        if destroyed == NO_EFFECT:
            return
        elif destroyed == DESTROYED:
            self.score += DESTROY_SCORE
        else:
            self.score += HIT_SCORE
    
    def draw(self, brick_count):
        Print([MOVE_CURSOR % (self.height, 1), ' '*50])
        Print([MOVE_CURSOR % (self.height, 1), 'Lives: ', self.lives, ' Score: ', self.score,
                ' Bricks Left: ', brick_count, ' Time: ', int(time.time() - self.start_time)])
        Print([MOVE_CURSOR % (self.height+5, 1)])
        
    def lose_life(self):
        self.lives -= 1
        
    def get_lives(self):
        return self.lives
    
    def try_powerup(self, position, ball, paddle):
        if random.uniform(0, 1) <= POWERUP_PROBABILITY:
            powerup = random.choice(self.powerups)
            if powerup == SHRINK_PADDLE:
                self.onscreen.append(ShrinkPaddle(self.height-4, position))
                self.onscreen[-1].draw()
            elif powerup == GROW_PADDLE:
                self.onscreen.append(GrowPaddle(self.height-4, position))
                self.onscreen[-1].draw()
            elif powerup == FAST_BALL:
                self.onscreen.append(FastBall(self.height-4, position))
            elif powerup == PADDLE_GRAB:
                self.onscreen.append(PaddleGrab(self.height-4, position))
    
    def move_powerup(self, ball, paddle):
        # Shifting powerups down and applying their effects
        for powerup in self.onscreen:
            powerup.undraw()
            ret = powerup.move(paddle)
            
            if ret == ADD_POWERUP:
                self.onscreen.remove(powerup)
                if powerup.type == SHRINK_PADDLE or powerup.type == GROW_PADDLE:
                    for temp in self.active:
                        if temp.type == SHRINK_PADDLE:
                            self.active.remove(temp)
                        if temp.type == GROW_PADDLE:
                            self.active.remove(temp)
                
                for temp in self.active:
                    if temp.type == powerup.type:
                        self.active.remove(temp)
                
                self.active.append(powerup)
                self.active[-1].apply_effect(ball, paddle)
                
            elif ret == KEEP_POWERUP:
                powerup.draw()                

            else:
                self.onscreen.remove(powerup)
                
        # Removing expired powerups
        for powerup in self.active:
            if powerup.expired():
                powerup.remove_effect(ball, paddle)
                self.active.remove(powerup)