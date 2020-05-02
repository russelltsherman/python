# Python Lists

Lists are the most versatile of Python's compound data types.

A list contains items separated by commas and enclosed within square brackets ([]).
All the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1.
The plus (+) sign is the list concatenation operator, and the asterisk (\*) is the repetition operator.

```py
# implicitly create dict type
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# explicitly create string type
a = list(["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"])

# get size of dict
print(len(thislist))  # => 7

# access the list items by referring to the index number:
print(thislist[1])  # => banana
print(thislist[-1])  # => mango
print(thislist[:4])  # => ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:])  # => ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1]) # => ['orange', 'kiwi', 'melon']

# iterate list
for x in thislist:
    print(x)

if "mango" in thislist:
    print("Yes, 'mango' is one of the values in the thislist list")

```

## List/Array Methods

Python has a set of built-in methods that you can use on lists/arrays.

| Method    | Description                                                                  |
| --------- | ---------------------------------------------------------------------------- |
| append()  | Adds an element at the end of the list                                       |
| clear()   | Removes all the elements from the list                                       |
| copy()    | Returns a copy of the list                                                   |
| count()   | Returns the number of elements with the specified value                      |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list |
| index()   | Returns the index of the first element with the specified value              |
| insert()  | Adds an element at the specified position                                    |
| pop()     | Removes the element at the specified position                                |
| remove()  | Removes the first item with the specified value                              |
| reverse() | Reverses the order of the list                                               |
| sort()    | Sorts the list                                                               |
