fruits = ["apple", "banana", "cherry", "orange", "grapes"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
    if x == "orange":
        break
for x in "banana":
    print(x)
for x in range(3, 9, 2):
    print(x)
else:
    print("Already printed!")
p = [1, 2, 3]
q = [1, 2, 3]
for i in p:
    for j in q:
        print(i, j)
for i in p:
    pass
