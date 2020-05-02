# Python Dictionaries

A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).

```py
# implicitly create dict type
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# explicitly create dict type
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment

# Get the value of the "model" key:
x = thisdict["model"]
x = thisdict.get("model")

# Change the "year" to 2018:
thisdict["year"] = 2018

# Add a key value pair
thisdict["color"] = "red"

# Remove a key value pair
thisdict.pop("clolor")

# get size of dict
print(len(thisdict))

# iterate discionary
for key in thisdict:
    value = thisdict[x]
    print(key)
    print(value)

for value in thisdict.values():
  print(value)

for key, value in thisdict.items():
  print(key, value)

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

```

## Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.

| Method       | Description                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| clear()      | Removes all the elements from the dictionary                                                                |
| copy()       | Returns a copy of the dictionary                                                                            |
| fromkeys()   | Returns a dictionary with the specified keys and value                                                      |
| get()        | Returns the value of the specified key                                                                      |
| items()      | Returns a list containing a tuple for each key value pair                                                   |
| keys()       | Returns a list containing the dictionary's keys                                                             |
| pop()        | Removes the element with the specified key                                                                  |
| popitem()    | Removes the last inserted key-value pair                                                                    |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| update()     | Updates the dictionary with the specified key-value pairs                                                   |
| values()     | Returns a list of all the values in the dictionary                                                          |
