# Write your code here

noDays = int(input("Days you've been driving: "))

noYears = int(noDays/365)

noWeeks = int(noDays%365/7)

noDay = int(noDays%365%7)

print("You've been driving for: ")

print("Years:", noYears)

print("Weeks:", noWeeks)

print("Days:", noDay)

