# is_prime function definition goes here

def is_prime(number) :
    prime = True
    for i in range(2, number) :
        if number % i == 0 :
            prime = False
            break
    return prime

num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message

if is_prime(num) :
    print(str(num) + " is a prime")
else :
    print(str(num) + " is not a prime")