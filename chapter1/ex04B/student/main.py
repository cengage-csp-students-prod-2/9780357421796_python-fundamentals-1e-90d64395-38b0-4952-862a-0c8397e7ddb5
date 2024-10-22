# Write your code here
"""
This script prints the multiplication table of a whole number
by the multiples of 2, from 1 to 10.
"""

# Get user input and cast it to an integer
whole_num = int(input("Enter a whole number: "))

# Print the top border
print("_" * 10)

# Print the multiplication table
for i in range(1, 11):
    result = whole_num * (i * 2)
    print(f"{whole_num} * {i * 2} = {result}")

# Print the bottom border
print("_" * 10)
