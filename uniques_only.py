'''provides functions to list unique items'''
from collections.abc import Hashable


def uniques_only(incoming):
    '''Return list of Unique Items'''
    chkset = set()
    chklst = []
    for i in incoming:
        found = False
        if isinstance(i, Hashable):
            if i in chkset:
                found = True
            else:
                chkset.add(i)
        else:
            if i in chklst:
                found = True
            else:
                chklst.append(i)
        if not found:
            yield i


if __name__ == "__main__":
    nums = [1, -3, 2, 3, -1]
    squares = (n**2 for n in nums)
    trylst = [
        [['a', 'b'], ['a', 'c'], ['a', 'b']],
        [1, 2, 2, 1, 1, 3, 2, 1],
        squares,
        [['a', 'b'], ['a', 'c'], ['a', 'b']]
        ]
    for chk in trylst:
        print(list(uniques_only(chk)))
