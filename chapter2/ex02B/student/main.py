# Write your code here

myString = input("Word to convert: ")
count = int(input("How many letters at the end of the word should be converted? "))
strStart = 0
strEnd = len(myString)
secStart =strEnd-count
str1=myString[strStart:secStart]
str2=myString[secStart:strEnd]
secCount=strEnd-count
strSect = myString[secCount:strEnd]
strWhole = str1 + str2.upper()
print(strWhole)