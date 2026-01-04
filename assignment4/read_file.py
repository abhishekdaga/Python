#Task 1: Read a File and Handle Errors
# Write a Python program that:
# Opens and reads a text file named sample.txt.

file = "sample.txt"
try:
    with open(file, "rt") as f:
        # Prints its content line by line.
        content = f.readlines()
        linecount = 1
        for line in content:
            line = line.rstrip()
            print(f"Line {linecount}: {line}")
            linecount += 1

#Handles errors gracefully if the file does not exist.
except FileNotFoundError:
    print(f"Error: The file {file} was not found")


