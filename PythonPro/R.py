a = 50
x = 200

def myfunc():
    x = 100
    global y
    y = 25
    print(x)
    print(a)
    print(y)
    def mylocalfunction():
        print(x)
        print(a)
        print(y)


    mylocalfunction()


myfunc()
print(x)
print(a)
print(y)
