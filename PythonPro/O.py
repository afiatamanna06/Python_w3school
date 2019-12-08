class MyClass:
    x = 5


clsmy = MyClass()
print(clsmy.x)


class Person:
    def __init__(kitty, name, age):
        kitty.name = name
        kitty.age = age

    def myfunction(habijabi):
        print("My name is:", habijabi.name)


p1 = Person("Afia", 18)
print(p1.name)
print(p1.age)
p1.age = 19
print(p1.age)
p1.myfunction()


class Mypass:
    pass
