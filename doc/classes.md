# Python Classes

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

```py
class Person:
    # object constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello my name is " + self.name)

    # class definitions cannot be empty
    # if you for some reason have a class definition with no content,
    # put in the pass statement to avoid getting an error.
    def empty(self):
        pass


p1 = Person("John", 36)
p1.hello()
```
