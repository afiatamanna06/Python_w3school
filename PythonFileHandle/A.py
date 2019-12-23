f = open("demo.txt", "a")
f.write("This is a demo file.")
f.write("I am writing it.")
f.close()


f = open("demo.txt", "r")
print(f.read())
