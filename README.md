# ASCII BrickBreaker
### How to start the game
Start up the game by running 
```
python3 main.py
```
in the directory where main.py is present.

### Controls
The controls are like most other 2D games, use 'A' and 'D' to move the paddle left and right, and space to release the ball. Additionally, use 'N' to skip a level if you wish to forfeit all available points. 
Each brick on destruction may spawn a powerup that can help or hinder your gameplay. 

**Shrink Paddle (S)**: 

This powerup decreases the paddle size giving the player a smaller surface to play with. 

**Grow Paddle (G)**:

This powerup increases the paddle size giving the player a larger surface to play with  

**Fast Ball (F)**:

This powerup increases the speed of the ball. 

**Paddle Grab (P)**:

This powerup gives the paddle the ability to make the ball stick to it, and release it at any point in time using the space key. 

**Thru Ball (T)**:

This powerup gives the ball the ability to phase through bricks, instantly destroying them (including the previously unbreakable bricks).

**Laser Paddle (L)**:

This powerup gives the paddle the ability to automatically fire lasers from its ends. The lasers damage the bricks the same way a ball would. 

**Fire Ball (E)**:

This powerup gives the ball an exploding property, and has the same effect as an exploding brick. 

### Modifications
The levels are drawn from the level<i>.dat file present in extra. It is fairly simple to create a map to play on, simply use numbers 1-3 to represent bricks of varying strength, 0 to represent free space, 4 to represent unbreakable bricks, 5 to represent exploding bricks and 6 to represent rainbow bricks. You could also choose to include a UFO in the game (makes it a lot more difficult) by entering a U in a level file. 
To increase/decrease the number of playable levels, change the ```NUM_LEVELS``` value in the ```src/defs.py``` file.

The file defs.py also contains several definitions which can be changed to change gameplay. Most notably, the paddle length, speed, max lives, scoring features, powerup probability and powerup duration can be tweaked to make gameplay easier/harder. 