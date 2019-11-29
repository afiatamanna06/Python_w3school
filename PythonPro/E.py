thisli = ['apple','banana','mango','grapes','cherry']
print(thisli)
print(thisli[1])
print(thisli[-1])
print(thisli[1:3])
print(thisli[:4])
print(thisli[2:])
print(thisli[-4:-1])
thisli[1] = "lemon"
print(thisli)
for x in thisli:
    print(x)
if "apple" in thisli:
    print("Apple present")
print(len(thisli))
thisli.append("orange")
print(thisli)
thisli.insert(2,"berry")
print(thisli)
mylist = thisli.copy()
flist = list(thisli)
thisli.remove("grapes")
print(thisli)
thisli.pop(2)
print(thisli)
del thisli[0]
print(thisli)
thisli.clear()
print(thisli)
print(mylist)
print(flist)
glist = [1, 2, 3]
hlist = flist+glist
print(hlist)
for x in glist:
    hlist.append(x)
print(hlist)
hlist.extend(glist)
print(hlist)
klist = list(("appi","fizzy","lemonade"))
print(klist)
print(hlist.count(2))
glist.reverse()
print(glist)
print(glist.index(2))
flist.sort()
print(flist)

