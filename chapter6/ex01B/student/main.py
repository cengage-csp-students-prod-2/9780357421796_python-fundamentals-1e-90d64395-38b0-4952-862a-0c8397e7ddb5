# Write your code here
myDict = dict()

def word_counter(myStringParm):
    myStringParm = myStringParm.strip()
    myStringParm = myStringParm.lower()
    for myLet in myStringParm:
        if myLet not in myDict:
            #myOccur = myLet
            myOccur=len(myStringParm.split()) - 1
            myDict[myLet]= myOccur
    print(myDict)
    
word_counter("Mississippi")
print(word_counter("Mississippi"))