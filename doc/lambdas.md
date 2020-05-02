# Python Lambdas

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

```py
# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))

# A lambda function that multiplies argument a with argument b and print the result:
x = lambda a, b : a * b
print(x(5, 6))

# A lambda function that sums argument a, b, and c and print the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# create functions with different behavior in a DRY fashion
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```
