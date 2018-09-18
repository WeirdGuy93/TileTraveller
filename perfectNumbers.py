numberToCheck = int(input("Write a number: "))

checker = 0
counter = 1
perfect = False

if numberToCheck > 0 :
    while counter < numberToCheck :

        if numberToCheck % counter == 0 :
            checker += counter

        counter+=1
    else:
        if checker < numberToCheck :
            result = " is deficient."

        elif checker > numberToCheck :
            result = " is abundant."
        else :
            result = " is perfect!"
    print(str(numberToCheck) + result)
else :
    print("All perfect numbers are above zero")