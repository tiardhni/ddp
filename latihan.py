class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, self.age)

y = Person("John", 30)
y.printname()

class Student(Person):
    pass

y = Student("John", 30)
y.printname()

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(self, name, age)
        self.graduationyear = grade

    def welcome(self):
        print("Welcome, my name is {0} and I am {1} years old.".format(self.name, self.age))

y = Student("John", 30, 2019)
y.welcome()
