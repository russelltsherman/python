# Python inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

## Create a Parent Class

Any class can be a parent class, so the syntax is the same as creating any other class:

```py
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```

## Create a Child Class

To create a class that inherits the functionality from another class,
send the parent class as a parameter when creating the child class:

```py
class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)
```

```py
x = Student("Mike", "Olsen", 2021)
x.welcome()
```
