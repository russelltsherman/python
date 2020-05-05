# Python itertools module

itertools — Functions creating iterators for efficient looping
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
Each has been recast in a form suitable for Python.

The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.
Together, they form an “iterator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python.

For instance, SML provides a tabulation tool: tabulate(f) which produces a sequence f(0), f(1), .... The same effect can be achieved in Python by combining map() and count() to form map(f, count()).

These tools and their built-in counterparts also work well with the high-speed functions in the operator module. For example, the multiplication operator can be mapped across two vectors to form an efficient dot-product: sum(map(operator.mul, vector1, vector2)).

## Infinite iterators:

| Iterator | Arguments     | Results                                        |
| -------- | ------------- | ---------------------------------------------- |
| count()  | start, [step] | start, start+step, start+2\*step, …            |
| cycle()  | p             | p0, p1, … plast, p0, p1, …                     |
| repeat() | elem [,n]     | elem, elem, elem, … endlessly or up to n times |

```py
count(10)
# => 10 11 12 13 14 ...
cycle('ABCD')
# => A B C D A B C D ...
repeat(10, 3)
# => 10 10 10
```

## Iterators terminating on the shortest input sequence:

| Iterator              | Arguments                   | Results                                    |
| --------------------- | --------------------------- | ------------------------------------------ |
| accumulate()          | p [,func]                   | p0, p0+p1, p0+p1+p2, …                     |
| chain()               | p, q, …                     | p0, p1, … plast, q0, q1, …                 |
| chain.from_iterable() | iterable                    | p0, p1, … plast, q0, q1, …                 |
| compress()            | data, selectors             | (d[0] if s[0]), (d[1] if s[1]), …          |
| dropwhile()           | pred, seq                   | seq[n], seq[n+1], starting when pred fails |
| filterfalse()         | pred, seq                   | elements of seq where pred(elem) is false  |
| groupby()             | iterable[, key]             | sub-iterators grouped by value of key(v)   |
| islice()              | seq, [start,] stop [, step] | elements from seq[start:stop:step]         |
| starmap()             | func, seq                   | func(*seq[0]), func(*seq[1]), …            |
| takewhile()           | pred, seq                   | seq[0], seq[1], until pred fails           |
| tee()                 | it, n                       | it1, it2, … itn splits one iterator into n |
| zip_longest()         | p, q, …                     | (p[0], q[0]), (p[1], q[1]), …              |

```py
accumulate([1,2,3,4,5])
# => 1 3 6 10 15
chain('ABC', 'DEF')
# => A B C D E F
chain.from_iterable(['ABC', 'DEF'])
# => A B C D E F
compress('ABCDEF', [1,0,1,0,1,1])
# => A C E F
dropwhile(lambda x: x<5, [1,4,6,4,1])
# => 6 4 1
filterfalse(lambda x: x%2, range(10))
# => 0 2 4 6 8
islice('ABCDEFG', 2, None)
# => C D E F G
starmap(pow, [(2,5), (3,2), (10,3)])
# => 32 9 1000
takewhile(lambda x: x<5, [1,4,6,4,1])
# => 1 4
zip_longest('ABCD', 'xy', fillvalue='-')
# => Ax By C- D-

```

## Combinatoric iterators:

| Iterator                        | Arguments          | Results                                                       |
| ------------------------------- | ------------------ | ------------------------------------------------------------- |
| product()                       | p, q, … [repeat=1] | cartesian product, equivalent to a nested for-loop            |
| permutations()                  | p[, r]             | r-length tuples, all possible orderings, no repeated elements |
| combinations()                  | p, r               | r-length tuples, in sorted order, no repeated elements        |
| combinations_with_replacement() | p, r               | r-length tuples, in sorted order, with repeated elements      |

```py
product('ABCD', repeat=2)
# => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)
# => AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)
# => AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)
# => AA AB AC AD BB BC BD CC CD DD
```
