f = open("demo.txt", "a")
f.write("This is a demo file.")
f.write("I am writing it.\n")
f.write("I'm just wonder if you love me.\n")
f.close()


f = open("demo.txt", "r")
print(f.read(5))
f.close()


f = open("demo.txt", "r")
print(f.read())
f.close()


f = open("demo.txt", "r")
print(f.readline())
f.close()


f = open("demo.txt", "r")
for x in f:
    print(x)
