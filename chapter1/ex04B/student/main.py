# Write your code here
"""
This is how we create a multiplication table
"""
# Get user input and cast it to an integer
whole_num = int(input("Type a whole number: "))

# Print top border
print("_" * 10)

# Print the whole number and its 2's multiplication table
for i in range(1, 11):
    print(f"{whole_num} x {i * 2} = {whole_num * (i * 2)}")

# Print bottom border
print("_" * 10)
