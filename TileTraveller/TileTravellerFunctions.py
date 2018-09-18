def get_available_directioins(x,y) :
    """ 
    In: x and y position
    This functioin takes in the players position on the x and y axis
    and returns a string that tells him which directions are available
    Out: string with available direction
    """

    avail_dir = []
    if x > 1 :
        avail_dir.append("(S)outh")    
    if x < 3 :
        avail_dir.append("(N)orth")
    if y > 1 :
        avail_dir.append("(E)ast")
    if y < 3 :
        avail_dir.append("(W)est")

    direction_string = "You can travel: "

    print("You can travel: ", end="")
    for i in range(0, len(avail_dir)) :
        direction_string += avail_dir[i] + " "
        if len(avail_dir) > i+1 :
            direction_string += "or "
    return direction_string

def move_the_player_if_valid(direction, x, y) :
    """
    In: string with desired direction and the current 
    position of the player
    
    Out: New grids or an error

    This function checks if the player chose a valid direction
    and returns the new position if it is.
    """

    direction = direction.lower()

    if direction == "s" :
        if y == 1 :
            return False
        else :
            y -= 1
    elif direction == "n" :
        if y == 3 :
            return False
        else :
            y += 1
    elif direction == "e" :
        if x == 1 :
            return False
        else :
            x -= 1
    elif direction == "w" :
        if x == 3 :
            return False
        else :
            x += 1

    return [x,y]

def check_if_game_is_won(x,y) :
    """
    In: position of the player
    Out: A boolean value

    This function checks if the game is won!
    """

    if x == 3 and y == 1 :
        return True
    else :
        return False