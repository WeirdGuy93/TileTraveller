#Algorithm
# while not finished
#     print directions
#     get input
#     validate input
#     update coords
#     check if finished
# Yay!


x = 1
y = 1

while x != 3 or y != 1:
    avail_dir = []
    if x > 1 :
        avail_dir.append("(S)outh")    
    if x < 3 :
        avail_dir.append("(N)orth")
    if y > 1 :
        avail_dir.append("(E)ast")
    if y < 3 :
        avail_dir.append("(W)est")
    print("You can travel: ", end="")
    for i in range(0, len(avail_dir)) :
        print(avail_dir[i], end=" ")
        if len(avail_dir) > i+1 :
            print("or", end=" ")
    print()
    movement = input("Direction: ")

    if movement.lower() == "s" :
        if x == 1 :
            print("Not a valid direction!")
        else :
            x -= 1
    elif movement.lower() == 'n' :
        if x == 3 :
            print("Not a valid direction!")
        else :
            x += 1
    elif movement.lower() == 'e' :
        if y == 1 :
            print("Not a valid direction!")
        else :
            y -= 1
    elif movement.lower() == "w" :
        if y == 3 :
            print("Not a valid direction!")
        else :
            y += 1

print("Victory!")