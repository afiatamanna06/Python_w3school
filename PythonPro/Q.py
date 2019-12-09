fruits = ("apple", "banana", "cherry")
f = iter(fruits)
print(next(f))
print(next(f))
print(next(f))
mystr = "banana"
it = iter(mystr)
print(next(it))
print(next(it))
print(next(it))
print("In for loop:")
for x in mystr:
    print(x)
