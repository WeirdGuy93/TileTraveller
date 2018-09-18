
counter = 10

while counter < 100 :
    
    new_num = counter**2
    if new_num < 1000 :
        if new_num % 100 == counter :
            print(counter)

    counter +=1
