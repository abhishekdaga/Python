#Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# Creates a dictionary where student names are keys and their marks are values.
students = {'Alice': 85, 'Bob': 80, 'Carol': 75, 'David': 88, 'Eve': 90}
# Asks the user to input a student's name.
student = input("Enter student's name: ").capitalize()

try:
    # Retrieves and displays the corresponding marks.
    print(f"{student}'s marks: {students[student]}")

# If the student’s name is not found, display an appropriate message.
except KeyError:
    print("Student not found.")

