# Write your code here
#name = input("Enter your name?")
#password = input("Enter your password")

#while name == "Josh":
    #if password == "Pas$Word":
    #print("Welcome back, Josh")
#else:
#    print("Incorrect password, try again...")

# main.py

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
