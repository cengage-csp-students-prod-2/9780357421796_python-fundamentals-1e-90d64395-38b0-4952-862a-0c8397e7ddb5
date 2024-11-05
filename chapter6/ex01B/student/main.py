# Write your code here
myDict = dict()

def word_counter(myStringParm):
    myDict = dict()
    myWord = ""
    myCount = 0
    myStringParm = myStringParm.strip()
    myStringParm = myStringParm.lower()
    parm_length = len(myStringParm)
    for myLet in myStringParm:
        if myLet not in myWord:
            myWord = myWord + myLet
            myCount = myCount + 1
            myDict.update({myLet:myCount})
    sorted(myDict)
    print(myDict)

word_counter("Mississippi")