# Write your code here
mySentence = input("Type a sentence: ")

myWord = input("Word to look for in sentence: ")

# Prepare the sentence for accurate counting
mySubString = mySentence.strip().lower()

# Count occurrences of the word
myCount = mySubString.count(myWord.lower())  # Also lowercase the search word

print("There are", myCount, "occurrences of", repr(myWord), "in the sentence.")
