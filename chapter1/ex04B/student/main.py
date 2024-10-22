# Write your code here
"""
This is how we create a multiplication table
"""
whole_num = int(input("Enter a whole number: "))

print("_" * 10)

for i in range(1, 11):
    result = whole_num * (i * 2)
    print(f"{whole_num} * {i * 2} = {result}")

print("_" * 10)
