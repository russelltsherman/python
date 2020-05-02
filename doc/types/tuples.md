# Python Tuples

A tuple is another sequence data type that is similar to the list.
A tuple consists of a number of values separated by commas.
Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are:
Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed
Tuples are enclosed in parentheses ( ( ) ) and are immutable.
Tuples can be thought of as read-only lists.

```py

# implicitly create set type
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# explicitly create set type
thistuple = tuple(["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"])

# get size of list
print(len(thistuple))  # => 7

# access the tuple items by referring to the index number:
print(thistuple[1])  # => banana
print(thistuple[-1])  # => mango
print(thistuple[:4])  # => ['apple', 'banana', 'cherry', 'orange']
print(thistuple[2:])  # => ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thistuple[-4:-1])  # => ['orange', 'kiwi', 'melon']

# iterate list
for x in thistuple:
    print(x)

if "mango" in thistuple:
    print("Yes, 'mango' is one of the values in the thistuple tuple")

```

## Python Tuple Methods

Python has two built-in methods that you can use on tuples.

| Method  | Description                                                                             |
| ------- | --------------------------------------------------------------------------------------- |
| count() | Returns the number of times a specified value occurs in a tuple                         |
| index() | Searches the tuple for a specified value and returns the position of where it was found |
