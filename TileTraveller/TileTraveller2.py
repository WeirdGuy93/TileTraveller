#https://github.com/WeirdGuy93/TileTraveller/tree/master/TileTraveller

import TileTravellerFunctions as functions

#Set starter position
x = 1
y = 1

#Set a bool to stop the game if won
game_won = False

while not game_won :
    #Print out the available directions
    print(functions.get_available_directions(x,y))
    
    #Get the direction the player wants to go
    player_move = input("Direction: ")

    new_position = functions.move_the_player_if_valid(player_move, x, y)

    # if the return type is "None" then the direction is not valid
    if new_position == None :
        print("This direction is not valid!")
    else :
        x = new_position[0]
        y = new_position[1]
    
    game_won = functions.check_if_game_is_won(x,y)

#Yay!
print("Victory!")