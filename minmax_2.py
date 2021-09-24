ISMISSING=object()

def minmax(lst, *, default = ISMISSING, key = lambda x:x ):
    if not default is ISMISSING:
        return (min(lst, key=key, default = default), max(lst, key=key, default=default))
    else:
        return (min(lst, key=key), max(lst, key=key))



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