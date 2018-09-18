import TileTravellerFunctions as functions

#Set starter position
x = 1
y = 1


game_won = False

while not game_won :

    print(functions.get_available_directioins(x,y))
    player_move = input("Direction: ")

    new_position = functions.move_the_player_if_valid(player_move, x, y)

    if not new_position :
        print("Not a valid position")
    else :
        x = new_position[0]
        y = new_position[1]
    game_won = functions.check_if_game_is_won(x,y)

print("Victory!")