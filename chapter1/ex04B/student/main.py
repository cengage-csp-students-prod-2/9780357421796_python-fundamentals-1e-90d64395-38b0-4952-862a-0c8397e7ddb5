"""
This is how we create a multiplication table
"""
# Getting the user input and converting it to an integer
whole_num = int(input("Generate a multiplication table for: "))

# Printing the top border
print("_" * 10)

# Printing the first line with the original number
print(f"Number: {whole_num}")

# Printing the multiplication table for multiples of 2 till 10
for i in range(2, 11, 2):
    print(f"{i}: {whole_num * i}")

# Printing the bottom border
print("_" * 10)