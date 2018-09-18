loan = float(input("Input the cost of the item in $: "))
month = 1
payment = 50.0
interests = 0.0
total_interests = 0.0

if loan > 1000 :
    interests_perc = 2.0
else :
    interests_perc = 1.5

while loan > 0 :

    
    interests = loan * (interests_perc / 100)

    loan += interests
    total_interests += interests
    if loan < 50 :
        payment = loan

    loan -= payment

    print("Month: " + str(month) + " Payment: " + str(round(payment,2)) + \
    " Interest paid: " + str(round(interests,2)) + \
    " Remaining debt: " + str(round(loan,2)))

    month +=1

print("")
print("Number of months: " + str(month -1))
print("Total interest paid: " + str(round(total_interests, 2)))