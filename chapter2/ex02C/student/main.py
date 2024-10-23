# Write your code here

mySentence = input("Type a sentence: ")
myWord= input("Word to look for in sentence: ")
mySubString = mySentence.strip()
mySubString = mySubString.lower()
myCount=mySubString.count(myWord)
print("There are", myCount, "occurences of", repr(myWord),"in the sentence.")