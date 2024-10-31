# Write your code here
cars = ('coupe', 'coupe', 'coupe', 'carbiolet', 'sedan')
x = cars.count('coupe')
print(x)
amt = len(cars)
print(amt)

stat = 0.45
if x/amt > stat:
    print("Too many coupes in the garage")
    else:
    print("You are all set with cars. to the terminal.")