# Write your code here
"""
This is how we create a multiplication table
"""
print("_" * 10)
whole_num = input("Type a whole number: ")

try:
    num = int(whole_num)
    print("_" * 10)
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("_" * 10)
except ValueError:
    print("Please enter a valid whole number.")
