#To Check if a Number is Even or Odd

# Take an integer input from the user
number = int(input("Enter a number: "))

#Checks whether the number is even or odd using an if-else statement and print result
if number % 2:
    print(f"{number} is an odd number.")
else:
    print(f"{number} is an even number.")
