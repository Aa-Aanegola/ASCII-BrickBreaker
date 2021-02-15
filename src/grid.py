from .paddle import Paddle
from .brick import Brick
from .ball import Ball
from .player import Player
from .defs import *

class Grid:
    def __init__(self, path):
        """
            Grid contains a grid of bricks
            Grid also stores the ball and paddle objects
        """
        
        # Initializing the display
        level_file = open(path, "r")
        level_text = level_file.read().split('\n')
        self.state = []
        for row in level_text:
            self.state.append([])
            for type in row:
                self.state[-1].append(Brick(int(type)))
        for i in range(EMPTY_ROWS):
            self.state.append([])
            for i in range(len(level_text[0])):
                self.state[-1].append(Brick(0))
        
        # Helper variables
        self.width = BRICK_LENGTH*len(self.state[0])
        self.height = len(self.state)
        
        # Variable to reset the game with a spacebar click
        self.reset = True
        
        # Initialising paddle
        self.paddle = Paddle(self.width // 2, self.height+1, self.width)
        
        # Initalising ball, the positions are 0 indexed
        self.ball = Ball(
            self.height,
            self.width//2 + 1 + random.randint(-PADDLE_LENGTH, PADDLE_LENGTH),
            self.width,
            self.height)    
        
        self.player = Player(self.height+4)
         
    def initialise_display(self):
        # Drawing the brick grid
        for row in self.state:
            for brick in row:
                Print([brick.color + ' '*BRICK_LENGTH, RESET])
            print()
        Print([RESET])
        
        # Drawing the paddle
        self.paddle.draw()
        
        # Drawing the ball
        self.ball.draw()    
        
        #Display player info
        self.player.draw(Brick.count)
        # Move the cursor outside the frame
        Print([MOVE_CURSOR % (self.height+3, 1), RESET])
    
    
    def update(self):
        if self.game_over():
            return False

        # Remove the ball from its current position
        self.ball.undraw()
    
        # Check for ball collisions        
        if self.reset == False:
            self.move_ball()
        
        
        self.player.move_powerup(self.ball, self.paddle, self.state)
        
        # Redraw the ball, the paddle and the player
        self.ball.draw()
        self.paddle.draw()
        self.player.draw(Brick.count)
      
        return True
      
    
    def use_keystroke(self, keystroke):
        if keystroke == ' ':
            self.reset = False
        if keystroke == 'a':
            can_move = self.paddle.move(LEFT)
            if self.reset and can_move:
                self.ball.undraw()
                self.ball.move(LEFT)

        elif keystroke == 'd':
            can_move = self.paddle.move(RIGHT)
            if self.reset and can_move:
                self.ball.undraw()
                self.ball.move(RIGHT)

        elif keystroke == 'q':
            return False 
        return True
    
    def move_ball(self):
        ball_position = self.ball.get_position()
        ball_velocity = self.ball.get_velocity()
        
        paddle_position, paddle_length = self.paddle.get_data()
        
        cur_y, cur_x = ball_position
        diff_y, diff_x = ball_velocity
        diff_y = abs(diff_y)
        diff_x = abs(diff_x)
        vel_y, vel_x = ball_velocity
        
        
        while diff_x or diff_y:
            bounds = self.get_bounds((cur_y, cur_x))
            #Print([MOVE_CURSOR % (self.height+3, 1), bounds])
              
            # bounce the ball
            break_r = False
            break_l = False
            break_u = False
            break_d = False
            
            if EXITED in bounds and vel_y > 0:
                self.reset_state()
                return
            
            elif cur_y == self.height and DFACE in bounds and vel_y > 0:
                if self.paddle.grab == True:
                    self.reset = True
                    self.ball.set_velocity((-1, cur_x - 1 - self.paddle.position))
                    return
                self.ball.set_velocity((-1, cur_x - 1 - self.paddle.position))
                if cur_x - 1 - self.paddle.position == 0:
                    diff_x = 0
                vel_y, vel_x = self.ball.get_velocity()
             
            elif diff_x != 0 and vel_x < 0:
             #   Print([MOVE_CURSOR % (self.height+6, 1), "left"])
                if LFACE in bounds:
                    break_l = True
                    vel_x *= -1
                else:
                    cur_x -= 1
                    diff_x -= 1
            
            elif diff_x != 0 and vel_x > 0:
              #  Print([MOVE_CURSOR % (self.height+6, 1), "right"])
                if RFACE in bounds:
                    break_r = True
                    vel_x *= -1
                else:
                    cur_x += 1
                    diff_x -= 1
            
            elif diff_y != 0 and vel_y < 0:
               # Print([MOVE_CURSOR % (self.height+7, 1), "up  "])
                if UFACE in bounds:
                    break_u = True
                    vel_y *= -1
                else:
                    cur_y -= 1
                    diff_y -= 1
            
            elif diff_y != 0 and vel_y > 0:
                #Print([MOVE_CURSOR % (self.height+7, 1), "down"])
                if DFACE in bounds:
                    break_d = True
                    vel_y *= -1
                else:
                    cur_y += 1
                    diff_y -= 1

            #Print([MOVE_CURSOR % (self.height+11, 0), break_d])
            scored = False
            destroyed = NO_EFFECT 
            position = None  
            if break_l and cur_x != 1:
                scored = True
                grid_y = cur_y - 1
                grid_x = (cur_x - 1)//BRICK_LENGTH - 1
                position = (cur_y+1, cur_x)
                destroyed = self.state[grid_y][grid_x].damage(grid_y, grid_x, self.state)
                
            if break_r and cur_x != self.width:
                scored = True
                grid_y = cur_y - 1
                grid_x = cur_x // BRICK_LENGTH
                position = (cur_y+1, cur_x)
                destroyed = self.state[grid_y][grid_x].damage(grid_y, grid_x, self.state)
                
            if break_u and cur_y != 1:
                scored = True
                grid_y = cur_y - 2
                grid_x = (cur_x-1) // BRICK_LENGTH
                position = (cur_y+1, cur_x)
                destroyed = self.state[grid_y][grid_x].damage(grid_y, grid_x, self.state)
                
            if break_d and cur_y != self.height-1:
                scored = True
                grid_y = cur_y
                grid_x = (cur_x-1) // BRICK_LENGTH
                position = (cur_y+1, cur_x)
                destroyed = self.state[grid_y][grid_x].damage(grid_y, grid_x, self.state)
                
            if scored:
                self.player.increment_score(destroyed)
                if destroyed == DESTROYED:
                    self.player.try_powerup(position, self.ball, self.paddle)
        
        new_position = (cur_y, cur_x)
        new_velocity = (vel_y, vel_x)
        self.ball.set_position(new_position)
        self.ball.set_velocity(new_velocity)
        
        return 
    
    
    def get_bounds(self, position):
        y, x = position
        ret = []
        
        #Print([MOVE_CURSOR % (self.height+5, 0), y, '    ',  x, '    '])
        # Handles both walls and bricks
        if y != self.height and self.state[y][(x-1)//BRICK_LENGTH].notEmpty():
            ret.append(DFACE)
        if y == 1 or self.state[y-2][(x-1)//BRICK_LENGTH].notEmpty():
                #Print([MOVE_CURSOR % (self.height+8, 1), "Hit Ceiling"])
            ret.append(UFACE)
            
        if x % BRICK_LENGTH == 0:
            if x == self.width or self.state[y-1][x//BRICK_LENGTH].notEmpty():
                ret.append(RFACE)
        if x % BRICK_LENGTH == 1:
            if x == 1 or self.state[y-1][(x-1)//BRICK_LENGTH].notEmpty():
                ret.append(LFACE)
        # Check for paddle
        paddle_position, paddle_length = self.paddle.get_data()
        if y == self.height and paddle_position-paddle_length <= x-1 <= paddle_position+paddle_length:
            ret.append(DFACE)
        elif y == self.height:
            ret.append(EXITED)
            
        ret = list(set(ret))
        
        return ret
    
    def reset_state(self):
        self.paddle.reset_position()
        self.player.lose_life(self.ball, self.paddle, self.state)
        self.ball.reset_position()
        self.reset = True
        
    def game_over(self):
        if self.player.get_lives() == 0:
            return True
        if Brick.count == 0:
            return True
        return False

    def display_message(self):
        Print([MOVE_CURSOR % (self.height+8, 1), 'Game Over!', MOVE_CURSOR % (self.height+9, 1)])