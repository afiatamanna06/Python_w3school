thistuple = ("apple", "banana", "cherry", "berry", "orange", "lemon", "grapes")
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:5])
print(thistuple[-5:-2])
y = list(thistuple)
y[1] = "strawberry"
y.append("jackfruit")
thistuple = tuple(y)
print(thistuple)
for x in thistuple:
    print(x)
if "apple" in thistuple:
    print("Apple found")
print(len(thistuple))
ftuple = ("meww",)
print(type(ftuple))
gtuple = ("meww")
print(type(gtuple))
#del ftuple
htuple = (1, 2, 3)
mtuple = ftuple + htuple
print(mtuple)
ktuple = tuple((7, 8, 9))
print(ktuple)
print(ktuple.count(9))
print(ktuple.index(9))
