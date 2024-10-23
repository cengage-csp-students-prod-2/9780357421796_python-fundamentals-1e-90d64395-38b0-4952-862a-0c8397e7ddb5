mySentence = input("Type a sentence: ")
myWord = input("Word to look for in sentence: ")
# Normalize both the sentence and the word to lowercase
mySubString = mySentence.strip().lower()
myWord = myWord.lower()
# Count occurrences of the word
myCount = mySubString.split().count(myWord)
print("There are", myCount, "occurrences of", repr(myWord), "in the sentence.")