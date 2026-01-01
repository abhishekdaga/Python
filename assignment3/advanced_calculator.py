#Using the Math Module for SquareRoot, Logarithm, and Sine Calculations
#Asks the user for a number as input.
"""
Uses the math module to calculate:
Square root of the number
Natural logarithm (log base e) of the number
Sine of the number (in radians)
"""
import math

number = int(input("Enter a number: "))
if number > 0:
    print(f"Square root: {math.sqrt(number)}")
    print(f"Logarithm: {math.log(number)}")
else: print("Number must be greater than or equal to zero for square root and logarithm.")
print(f"Sine: {math.sin(number)}")