# Reeborg’s World Maze Solver (Right-Hand Rule)
# Run this in https://reeborg.ca/ using "Maze" world

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Move forward until a wall is hit
while front_is_clear():
    move()
turn_left()

# Follow the right-hand rule
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
