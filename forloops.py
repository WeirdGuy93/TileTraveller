stars = int(input("Max number of stars: ")) # Do not change this line

starStr = ""

for i in range(1, stars+1) :
    starStr += "*"
    print(starStr)

for i in range(stars-1, 0, -1) :
    print(starStr[:i])