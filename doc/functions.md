# Python Functions

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:

```py
def my_function():
  print("Hello from a function")

```

## Arbitrary Arguments, \*args

```py
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

```

## Keyword Arguments, \*\*kwargs

```py
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

```

## The pass Statement

function definitions cannot be empty,
but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.

```py
def myfunction():
  pass

```
