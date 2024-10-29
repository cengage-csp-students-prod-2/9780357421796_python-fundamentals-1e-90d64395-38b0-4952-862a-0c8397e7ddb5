# Write your code here
"""
This is how we create a multiplication table
"""
whole_num = int(input("Type a whole number: "))
print("_" * 10)
for i in range(1, 11):
    print(f"{whole_num} x {i * 2} = {whole_num * (i * 2)}")
print("_" * 10)
