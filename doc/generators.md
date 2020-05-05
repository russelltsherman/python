# Python Generator

## generator expression

Experience with list comprehensioons has shown their wide-spread ability throughout python.

However, many of the use cases do not need to have a full list created in memory.

Instead they only need to iterare over the element one at a time.

```py
g = (x*x for x in range(10))
print(g)
#  => <generator object <genexpr> at 0x10a5234d0>
```

## generator function

Generators are a simple tool for creating iterators.

They are written like regular functions but use the yeild statement whenever they want to return data

```py
def count(start,end):
    i=0
    while i < end:
        yield i
        i = i+i

g = count(0, 10)
print(g)
#  => <generator object count at 0x106f17550>
```
