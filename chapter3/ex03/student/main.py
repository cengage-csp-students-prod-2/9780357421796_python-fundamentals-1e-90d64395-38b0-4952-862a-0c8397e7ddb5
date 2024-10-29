# Write your code here

name = input("Enter your name: ")
password = "Pas$Word"
first = True

while True:
    user_input = input("Enter your password: ")
    if user_input == password:
        print(f"Welcome back, {name}")
        break
    else:
        print("Incorrect password, try again...")
