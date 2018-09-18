import math

verkefni = int(input("Hvaða verkefni viltu prófa?"))
	 

if verkefni == 1:
	
	m_str = input('Input m: ')  # do not change this line
	# change m_str to a float
	# remember you need c
	# e = 
	mass_float = float(m_str)

	e = mass_float * (300000000 ** 2)

	print("e =", e)  # do not change this line

elif verkefni == 2:

	in_str = input("Input s: ")
	in_int = int(in_str)
	print("in_int = ", in_int)
	in_float = float(in_str)
	print("in_float = ", in_float)


elif verkefni == 3:

	x1_str = input("Input x1: ")  # do not change this line
	y1_str = input("Input y1: ")  # do not change this line
	x2_str = input("Input x2: ")  # do not change this line
	y2_str = input("Input y2: ")  # do not change this line

	x1 = int(x1_str)
	y1 = int(y1_str)
	x2 = int(x2_str)
	y2 = int(y2_str)

	d = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2)) 
	print("d =",d)  # do not change this line

elif verkefni == 4:

	x_str = input("Input x: ")
	# remember to convert to an int
	first_three = int(x_str) // 1000
	last_two = int(x_str) % 100
	middle_two = ((int(x_str) // 100) % 100)
	print("original input:", x_str)
	print("first_three:", first_three)
	print("last_two:", last_two)
	print("middle_two:", middle_two)

elif verkefni == 5:

	secs_str = input("Input seconds: ") # do not change this line
	hours = (int(secs_str) // 3600) 
	minutes = (int(secs_str) // 60 - hours * 60)
	seconds =  (int(secs_str) % 60)

	print(hours,":",minutes,":",seconds) # do not change this line

elif verkefni == 6:

	weight_str = input("Weight (kg): ") # do not change this line
	height_str = input("Height (cm): ") # do not change this line

	height_str = (int(height_str) / 100)

	bmi = (float(weight_str) / (float(height_str) ** 2))

	print("BMI is: ", bmi) # do not change this line

elif verkefni == 7:

	years_str = input("Years: ") # do not change this line

	original_population = 307357870

	years_int = int(years_str)
	seconds = years_int * 365 * 24 * 60 * 60

	births = seconds // 7
	deaths = seconds // 13
	immigrants = seconds // 35

	new_population = original_population + births + immigrants - deaths

	print("New population after", years_int, " years is ", int(new_population)) # do not change this line

else:
	print("Það er ekkert verkefni með þetta númer.")
