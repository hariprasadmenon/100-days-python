def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    while wall_in_front()==1:
        turn_left()
        move()
        if wall_on_right():
            move()
        else:
            turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

