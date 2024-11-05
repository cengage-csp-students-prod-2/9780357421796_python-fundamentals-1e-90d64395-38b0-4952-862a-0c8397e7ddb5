# Write your code here
v = set({"car", "bus", "train"})
print(v)

v.add("bicycle")
print(v)

for veh in v:
    print(veh)

print(v.pop())

v.remove("car")
print(v)

v.clear()
print(v)