#Write a Python program that:

#Takes user input and writes it to a file named output.txt.
user_input1 = input("Enter text to write to the file: ")
file_name = "output.txt"
with open(file_name, "wt") as f:
    f.write(user_input1)
    print(f"Data successfully written to {file_name}")

user_input2 = input("Enter additional text to append: ")
#Appends additional data to the same file.
with open(file_name, "at") as f:
    f.write(user_input2)
    print(f"Data successfully appended")

#Reads and displays the final content of the file.
with open(file_name, "rt") as f:
    content = f.read()

print(f"Final content of {file_name} is: \n{content}")