ISMISSING=object()
from collections import namedtuple

MinMax = namedtuple("MinMax","min max")

def minmax(*iterable, default = ISMISSING, key = lambda x:x ):

    lst=list(iterable)
    if len(lst) == 0:
        raise TypeError("Must supply arguments")
    elif len(lst) == 1:
        lst = list(next(iter(lst)))
    if not default is ISMISSING:
        mm = MinMax (min(lst, key=key, default = default), max(lst, key=key, default=default))
    else:
        mm = MinMax (min(lst, key=key), max(lst, key=key))
    return mm



assert minmax([0, 1, 2, 3, 4]) == (0, 4)
assert minmax([], default=0) == (0,0)
assert minmax([10, 8, 7, 5.0, 3, 6, 2], default=0) == (2,10)
try:
    minmax([])
except ValueError:
    print("Good - error thrown.")
words = ["hi", "HEY", "Hello"]
assert minmax(words) == ('HEY', 'hi')
assert minmax(words, key=lambda s: s.lower()) == ("Hello","hi")
assert minmax(words, key=len) == ("hi","Hello")

numbers = {8, 7, 5, 3, 9, 6, 2}
assert minmax(numbers) == (2,9)
assert minmax(n**2 for n in numbers) == (4,81)
assert minmax([3], [2, 5], [4, -1]) == MinMax(min=[2, 5], max=[4, -1])