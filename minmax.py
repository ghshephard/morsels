import collections
def minmax(values, *, key=None):
    if not values:
        raise ValueError("Empty List")
    if not key:
        key = lambda x:x
    if isinstance(values, collections.abc.Iterator):
        values=list(values)
    mm = collections.namedtuple("mm", "min max")
    return mm(min(values, key=key), max=max(values, key=key))


if __name__ == "__main__":
    assert minmax([0, 1, 2, 3, 4]) == (0,4)
    assert minmax([10, 8, 7, 5.0, 3, 6, 2]) == (2,10)
    try: 
        minmax([])
    except ValueError:
        print("Success - Raised Value Error on Empty List.")
    words = ["hi", "HEY", "Hello"]
    assert minmax(words, key=lambda s: s.lower()) == ('Hello', 'hi')
    assert minmax(words, key=len) == ('hi', 'Hello')
    try:
         minmax([1], lambda x: x)
    except TypeError:
        print("Success -- Raised Type Error on non-named key.")
    numbers = {8, 7, 5, 3, 9, 6, 2}
    assert minmax(numbers) == (2,9)
    assert minmax(n**2 for n in numbers) == (4,81)
    mm = minmax([3, 2, 5, 4, -1])
    assert mm.min == -1
    assert mm.max == 5
    smallest, largest = mm 
    assert smallest == -1
    assert largest == 5


        
        