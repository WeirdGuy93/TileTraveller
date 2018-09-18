position = int(input("Input a position between 1 and 10: "))

Min = 1
Max = 10

keep_moving = True

if not Min < position < Max :
    print("Invalid position.")
    exit()

def new_position(input, position) :
    if input == "l" and position > Min:
        position -= 1
    elif input == "r" and position < Max :
        position += 1

    return position

def options() :
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    
def check_input(input) :
    if input == "l" or input == "r" :
        return True
    else :
        return False

while keep_moving:

    options()
    direction = input("Input your choice: ")
    keep_moving = check_input(direction)
    position = new_position(direction, position)
    print("New position is: " + str(position))
