#Calculate Factorial Using a Function

#Function factorial that takes a number as an argument
#calculates its factorial using a loop or recursion.

def factorial(n):
    if n == 0:
        #Returns the calculated factorial.
        return 1
    # Returns the calculated factorial.
    return n * factorial(n-1)

number = int(input("Enter a number: "))

if number >= 0:
    factorial_number = factorial(number)
    print(f"The factorial of {number} is {factorial_number}")
else:
    print("Number must be greater than or equal to zero.")
