import TileTravellerFunctions as functions

#Set starter position
x = 1
y = 1

#Set a bool to stop the game if won
game_won = False

while not game_won :
    #Print out the available directions
    print(functions.get_available_directioins(x,y))
    
    #Get the direction the player wants to go
    player_move = input("Direction: ")

    new_position = functions.move_the_player_if_valid(player_move, x, y)

    if not new_position :
        print("Not a valid direction!")
    #Update coordinates if the direction is valid
    else :
        x = new_position[0]
        y = new_position[1]
    
    game_won = functions.check_if_game_is_won(x,y)

#Yay!
print("Victory!")