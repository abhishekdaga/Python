#Task 2: Demonstrate List Slicing

# Write a program to create a list of numbers from 1 to 10.

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Extract the first five elements from the list.

extracted_list = list_numbers[0:5:1]

# Reverse the extracted elements.
reversed_list = extracted_list[::-1]

# Print original, extracted, and reversed list.
print(f"The original list: {list_numbers}")
print (f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")
