"""
This is how we create a multiplication table
"""
whole_num = int(input("Generate a multiplication table for: "))
print("_" * 10)
print(f"Number: {whole_num}")
for i in range(2, 11, 2):
    print(f"{i}: {whole_num * i}")
print("_" * 10)