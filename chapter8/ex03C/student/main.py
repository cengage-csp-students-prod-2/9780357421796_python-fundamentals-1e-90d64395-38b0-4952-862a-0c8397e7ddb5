import random
# Write your function here

def number_randomizer(NumberOfTimes):
    randos = []
    for x in range(NumberOfTimes):
        randos.append(random.randrange(1, 100))
    return randos

print(number_randomizer(2)) 
print(number_randomizer(4))
print(number_randomizer(6))
