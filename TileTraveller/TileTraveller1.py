#Algorithm
# 
# while not finished
#     print directions
#     get input
#     validate input
#     update coords
#     check if finished
# Yay!

#1.
#   Longer code is always harder to read. Althou this code is very 
#   straight forward and easy to read (barely any use for comments even)
#   as soon as it's gets just a little bit more complicated (just 1 more
#   row up and to the side with an extra blockade) the code gets longer 
#   and longer and therefore harder to read,
#
#    If we make a function for each step we're dividing it into "chapters",
#    making the main program much easier to read ba making each step more
#    straight forward. (with well named functions)
#    The functions make the code inside them easier to read because they
#    only have one objective.



x = 1
y = 1

while x != 3 or y != 1:

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


    avail_dir = []
    if south :
        avail_dir.append("(S)outh")    
    if north :
        avail_dir.append("(N)orth")
    if east :
        avail_dir.append("(E)ast")
    if west :
        avail_dir.append("(W)est")

    print("You can travel:", end=" ")
    for i in range(len(avail_dir)) :
        print(avail_dir[i], end=" ")
        if len(avail_dir) > i+1 :
            print("or", end=" ")
    print()
    
    movement = input("Direction: ").lower()

    if movement == "s" and south :
        y -= 1
    elif movement == "n" and north:
        y += 1
    elif movement == "e" and east:
        x += 1
    elif movement == "w" and west:
        x -= 1
    else :
        print("Not a valid direction!")

print("Victory!")