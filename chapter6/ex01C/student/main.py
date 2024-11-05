# Write your code here
veg1 = {0: 'Carrot', 1: 'Raddish'}
veg2 = {2: 'Beet', 3: 'Potato'}

def content_combiner (myDict1, myDict2):
    myGardenDict = myDict1 | myDict2
    return myGardenDict

myOutput = content_combiner(veg1,veg2)
print(myOutput)