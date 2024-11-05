# Write your code here
y = [2, 4, 6, 8]
x = [3, 6, 9, 12]

def unite_lists():
    z = set(x).union(set(y))
    print(z)

unite_lists()
