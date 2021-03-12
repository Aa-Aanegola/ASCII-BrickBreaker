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
        self.laser = False
        self.last_shot = 0
        self.shots = []
        
    # Sets the length of the paddle
    def shrink(self):
        self.length = MIN_PADDLE_LENGTH
    
    def grow(self):
        if self.position - MAX_PADDLE_LENGTH < 0:
            self.position += 1
        if self.position + MAX_PADDLE_LENGTH > self.bound:
            self.position -= 1
        
        self.length = MAX_PADDLE_LENGTH
    
    def update_lasers(self, state, player):
        for shot in self.shots:
            y, x = shot 
            Print([MOVE_CURSOR % (y, x), ' '])
            Print(MOVE_CURSOR % (self.height+3, 0))
        
        if self.laser == False:
            return
        
        for shot in self.shots:
            y, x = shot
            if state[y-2][(x-1)//3].notEmpty():
                ret = state[y-2][(x-1)//3].damage(y-2, (x-1)//3, state, False, False, False)
                if ret == DAMAGED:
                    player.score += HIT_SCORE
                elif ret == DESTROYED:
                    player.score += DESTROY_SCORE
                self.shots.remove((y, x))
            elif y == 2:
                self.shots.remove((y, x))
            else:
                self.shots.remove((y, x))
                self.shots.append((y-1, x))
                
        if int(time.time()) - self.last_shot > LASER_INTERVAL:
            self.last_shot = int(time.time())
            self.shots.append((self.height-2, self.position - self.length+1))
            self.shots.append((self.height-2, self.position + self.length+1))
        
        for shot in self.shots:
            y, x = shot 
            Print([MOVE_CURSOR % (y, x), 'I'])
    
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
              ' '*(self.bound - self.length - self.position+2),
              RESET
        ])
        if self.laser:
            Print([MOVE_CURSOR % (self.height-1, 0), 
                   ' '*(self.position-self.length),
                   self.color + ' ',
                   RESET,
                   ' '*(self.length*2-1),
                   self.color + ' ',
                   RESET, 
                   ' '*(self.bound - self.length - self.position+2),])
        Print(MOVE_CURSOR % (self.height+3, 0))
    
    def move(self, direction):
        if self.position - self.length + direction < 0:
            return False
        if self.position + self.length + direction >= self.bound:
            return False 
        self.position += direction
        return True

    def reset_position(self):
        self.position = self.bound//2 + 1
        self.reset_length()

    def get_data(self):
        return (self.position, self.length)
        