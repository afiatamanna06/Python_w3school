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


class MyClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


mycls = MyClass()
myitra = iter(mycls)

print(next(myitra))
print(next(myitra))
print(next(myitra))

for x in myitra:
    print(x)
