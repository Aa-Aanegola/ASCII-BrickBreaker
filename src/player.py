from .defs import *
from .powerups import *
from .paddle import Paddle
from .brick import Brick, UFO
from .ball import Ball

class Player:
    def __init__(self):
        self.lives = MAX_LIVES
        self.score = 0
        self.height = None
        self.width = None
        self.start_time = time.time()
        self.powerups = POWERUP_LIST
        self.active = []
        self.onscreen = []
        
    def increment_score(self, destroyed):
        if destroyed == NO_EFFECT:
            return
        elif destroyed == DESTROYED:
            self.score += DESTROY_SCORE
        elif destroyed == UFO_DESTROYED:
            self.score += UFO_SCORE
        else:
            self.score += HIT_SCORE
    
    def draw(self, brick_count):
        Print([MOVE_CURSOR % (self.height, 1), ' '*50])
        Print([MOVE_CURSOR % (self.height, 1), 'Lives: ', self.lives, ' Score: ', self.score,
                ' Bricks Left: ', brick_count, ' Time: ', int(time.time() - self.start_time)])
        Print([MOVE_CURSOR % (self.height+5, 1)])
        
    def lose_life(self, ball, paddle, state):
        self.lives -= 1
        
        for powerup in self.active:
            powerup.remove_effect(ball, paddle, self)
            self.active.remove(powerup)
        
        for powerup in self.onscreen:
            y, x = powerup.position
            powerup.undraw(state[y-1][(x-1)//3].color)
            self.onscreen.remove(powerup)
        
    def new_level(self, ball, paddle, state):
        for powerup in self.active:
            powerup.remove_effect(ball, paddle, self)
            self.active.remove(powerup)
        
        for powerup in self.onscreen:
            y, x = powerup.position
            powerup.undraw(state[y-1][(x-1)//3].color)
            self.onscreen.remove(powerup)
        
    def get_lives(self):
        return self.lives
    
    def try_powerup(self, position, ball, paddle):
        ball_y, ball_x = ball.velocity
        velocity = (int(abs(ball_y)), ball_x)
        if random.uniform(0, 1) <= POWERUP_PROBABILITY:
            powerup = random.choice(self.powerups)
            if powerup == SHRINK_PADDLE:
                self.onscreen.append(ShrinkPaddle(self.height-4, self.width, velocity, position))
                self.onscreen[-1].draw()
            elif powerup == GROW_PADDLE:
                self.onscreen.append(GrowPaddle(self.height-4, self.width, velocity, position))
                self.onscreen[-1].draw()
            elif powerup == FAST_BALL:
                self.onscreen.append(FastBall(self.height-4, self.width, velocity, position))
            elif powerup == PADDLE_GRAB:
                self.onscreen.append(PaddleGrab(self.height-4, self.width, velocity, position))
            elif powerup == THRU_BALL:
                self.onscreen.append(ThruBall(self.height-4, self.width, velocity, position))
            elif powerup == LASER_PADDLE:
                self.onscreen.append(LaserPaddle(self.height-4, self.width, velocity, position))
            elif powerup == FIRE_BALL:
                self.onscreen.append(FireBall(self.height-4, self.width, velocity, position))
    
    def spawn_bomb(self, position):
        self.onscreen.append(Bomb(self.height-4, self.width, (1, 0), position))
    
    def move_powerup(self, ball, paddle, state):
        # Shifting powerups down and applying their effects
        for powerup in self.onscreen:
            y, x = powerup.position
            y = int(y)
            x = int(x)
            powerup.undraw(state[y-1][(x-1)//3].color)
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
                self.active[-1].apply_effect(ball, paddle, self)
                
            elif ret == KEEP_POWERUP:
                powerup.draw()                

            else:
                self.onscreen.remove(powerup)
                
        # Removing expired powerups
        for powerup in self.active:
            if powerup.expired():
                powerup.remove_effect(ball, paddle, self)
                self.active.remove(powerup)