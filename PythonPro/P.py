class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def function(self):
        print(self.fname, self.lname)


p1 = Person("Afia", "Anjum")
p1.function()


class Student(Person):
    pass


x = Student("Afra", "Anjum")
x.function()


class Teacher(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


y = Teacher("Sudipto", "Basu")
y.function()


class Actor(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

    def message(self):
        print("Welcome!", self.fname, self.lname)


z = Actor("Shahrukh", "Khan", 54)
z.function()
print(z.age)
z.message()
