from collections.abc import Iterable

def deep_flatten(seq):
    if type(seq) == str:
        yield seq
    else:
        for item in seq:
            if isinstance(item,Iterable):
                for element in deep_flatten(item):
                    yield element
            else:
                yield item
            


if __name__ == "__main__":
    assert list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert list(deep_flatten([[1, [2, 3]], 4, 5])) == [1, 2, 3, 4, 5]
