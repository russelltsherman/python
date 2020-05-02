# Python for loop

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

## Looping Through a String

Even strings are iterable objects, they contain a sequence of characters:

```py
for x in "banana":
    print(x)
```

## The break Statement

With the break statement we can stop the loop before it has looped through all the items:

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
```

## The continue Statement

With the continue statement we can stop the current iteration of the loop, and continue with the next:

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
```

## The range() Function

To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

```py
for x in range(6):
    print(x)
```

## Else in For Loop

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

```py

for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

## The pass Statement

for loops cannot be empty, but if you for some reason have a for loop with no content,
put in the pass statement to avoid getting an error.

```py
for x in [0, 1, 2]:
    pass
```
