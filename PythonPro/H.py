thiscls = {
    "Name" : "Aaaaa",
    "Class" : 7,
    "Section" : "A",
    "Year" : 2019
}
print(thiscls)
print(thiscls["Section"])
print(thiscls.get("Name"))
thiscls["Class"] = 8
print(thiscls)
for x in thiscls:
    print(x,thiscls[x])
for x in thiscls.values():
    print(x)
for x, y in thiscls.items():
    print(x, y)
if "Section" in thiscls:
    print("Section present")
print(len(thiscls))
thiscls["Shift"] = "Morning"
print(thiscls)
mycls = thiscls.copy()
print(mycls)
pdict = dict(thiscls)
print(pdict)
thiscls.pop("Year")
print(thiscls)
thiscls.popitem()
print(thiscls)
del thiscls["Section"]
print(thiscls)
thiscls.clear()
print(thiscls)
child1 = {
    "Name" : "Robert",
    "Year" : 1996
}
child2 = {
    "Name" : "Sirimon",
    "Year" : 1999
}
family = {
    "Child1" : child1,
    "Child2" : child2
}
print(family)
gdict = dict(Name="Hathway", Year=2011)
print(gdict)
xkey = ('key1', 'key2', 'key3')
ykey = 0
posdict = dict.fromkeys(xkey, ykey)
print(posdict)
x = posdict.keys()
print(x)
posdict.update({ "key4" : 0 })
print(posdict)
print(posdict.values())
