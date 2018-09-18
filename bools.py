verkefni = int(input("Hvaða verkefni viltu prófa?"))
	 

if verkefni == 1:

	num = int(input("Input a number: ")) # Do not change this line

	if num :
	    print(True) # Do not change this line
	else :
	    print(False) # Do not change this line   

elif verkefni == 2:

	num = int(input("Input a number: ")) # Do not change this line

	if num < 0 :
	    print("Negative") # Do not change this line
	elif num > 0 :
	    print("Positive") # Do not change this line
	else :    
	    print("Zero") # Do not change this line

elif verkefni == 3:

	num1 = int(input("First number: ")) # Do not change this line
	num2 = int(input("Second number: ")) # Do not change this line
	num3 = int(input("Third number: ")) # Do not change this line

	if num1 > num2 :
	    if num2 > num3 :
	        max_int = num1
	    elif num3 > num1:
	        max_int =  num3
	    else : num1 = max_int
	elif num2 > num3 :
	    max_int = num2
	else :
	    max_int = num3
	    
	print("The maximum is: ", max_int) # Do not change this line

elif verkefni == 4:

	grade = float(input("Input a grade: ")) # Do not change this line

	# Fill in the missing code below
	if grade > 10 or grade < 0 :
		print("Invalid grade!") # Do not change this line
	elif grade >= 5 :
		print("Passing grade!") # Do not change this line
	else :
		print("Failing grade!") # Do not change this line

elif verkefni == 5:

	year = int(input("Input a year: ")) # Do not change this line

	leap_year = False

	if (year % 4) == 0 :
		if (year % 100) == 0 :
			if (year % 400) == 0 :
				leap_year = True
		else :
			leap_year = True
	print(leap_year)

elif verkefni == 6:

	d1 = int(input("Input first dice: ")) # Do not change this line
	d2 = int(input("Input second dice: ")) # Do not change this line

	dsum = d1 + d2

	if d1 < 1 or d1 > 6 or d2 < 1 or d2 > 6 :
		print("Invalid input")
	elif dsum == 7 or dsum == 11 :
		print("Winner")
	elif dsum == 2 or dsum == 3 or dsum == 12 :
		print("Loser")
	else :
		print(dsum)

elif verkefni == 7:

	age = int(input("Input age: ")) # Do not change this line
	price = float(30)
	if age > 6 :
		if age >= 65:
			price = price * 0.50
	else:
		price = float(0)
	print(price)

else:
	print("Það eru bara 7 verkefni")