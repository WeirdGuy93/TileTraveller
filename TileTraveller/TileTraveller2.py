#https://github.com/WeirdGuy93/TileTraveller/tree/master/TileTraveller
# 1.
#   The first one was easier to implement, it's actually less code
#   and it didn't require the thought of "how far can I break it 
#   down".
# 2. 
#   My answer to the question in tile traveller 1 answers and explains
#   this.
# 3. 
#   I didn't really have any problems in the first one, I think.
#   This is making me doubt myself thou. Feel like I'm missing something.

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

    #Get the new player position
    new_position = functions.move_the_player_if_valid(player_move, x, y)
    #Set the new variable 
    x = new_position[0]
    y = new_position[1]

    game_won = functions.check_if_game_is_won(x,y)

#Yay!
print("Victory!")