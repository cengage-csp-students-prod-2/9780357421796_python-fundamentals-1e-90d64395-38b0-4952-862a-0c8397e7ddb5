# Write your code here
for x in range(10,101):
    if x == 0:
        pass
    if(x%5)!= 0:
        continue
    if type(x) != int:
        continue
    if x == 95:
        break
    else:
        print(x)