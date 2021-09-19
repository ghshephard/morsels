from collections.abc import Iterable

def deep_flatten(seq):
    for item in seq:
        if isinstance(item,Iterable) and not isinstance(item, (str, bytes)):
            yield from deep_flatten(item)
        else:
            yield item
            


if __name__ == "__main__":
    assert list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert list(deep_flatten([[1, [2, 3]], 4, 5])) == [1, 2, 3, 4, 5]
    print (list(deep_flatten([[[ 1,2, [3,4,(4.1, 4.2)],5],6],(7,8),range(12,15)])))