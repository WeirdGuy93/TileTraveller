def available_directions(x,y) :
    """
    In: x and y
    Out: available directions

    This function is only used by other functions to get
    the direction the player is allowed to move in.
    """
    south = True
    north = True
    east = True
    west = True

    if y == 1 or (x == 3 and y == 2) :
        east, west = False, False
    if y == 3:
        north = False
    if y == 2 and x == 2 :
        north, east = False, False
    if y == 1 or (x == 2 and y == 3) :
        south = False
    if x == 1 :
        west = False
    if x == 3 :
        east = False

    avail_dir = [north, south, east, west]
	
    return avail_dir

def get_directions_string(x,y) :
    """ 
    In: x and y position
    Out: string with available direction
    This function gets the available directions from the function: 
    "available_directions" and returns a nicely readable string
    """
    avail_dir = available_directions(x,y)
    
    direction_string = "You can travel: "

    if avail_dir[0] :
        avail_dir.append("(N)orth ")
    if avail_dir[1] :
        avail_dir.append("(S)outh ")
    if avail_dir[2] :
        avail_dir.append("(E)ast ")
    if avail_dir[3] :
        avail_dir.append("(W)est ")

    for i in range(len(avail_dir)) :
        direction_string += avail_dir[i] + " "
        if len(avail_dir) > i+1 :
            direction_string += "or "
    return direction_string

def move_the_player_if_valid(direction, x, y) :
    """
    In: string with desired direction and the current 
    position of the player
    
    Out: x and y (prints out if the desired direction is unavailable)

    This function checks if the player chose a valid direction
    and returns the position of the player.
    """

    direction = direction.lower()

    avail_dir = available_directions(x,y)

    if direction == "n" and avail_dir[0] :
        y += 1
    elif direction == "s" and avail_dir[1] :
        y -= 1
    elif direction == "e" and avail_dir[2] :
        x += 1
    elif direction == "w" and avail_dir[3] :
        x -= 1
    else :
        print("Not a valid direction!")

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
