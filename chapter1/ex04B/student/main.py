# Write your code here
"""
This is how we create a multiplication table
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
