from datetime import timedelta
from collections.abc import Iterable


def deep_add(lst, start=0):
    tot = start
    for i in lst:
        if isinstance(i,Iterable):
            tot = deep_add(i, tot)
        else:
            tot += i
    return tot




test_lists = [[[1, 2, 3, 4], 0],
    [[[1, 2, 3], [4, 5, 6]],0],
    [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],0],
    [[1, [2, [3, 4], [], [[5, 6], [7, 8]]]],0],
    [[[], []],0],
    [[(1, 2), [3, {4, 5}]],0],
    [[[[1, 2], [3, 4]], 2],0],
    [[[timedelta(5), timedelta(10)], [timedelta(3)]], timedelta(0)],
    [[1, [2, None]],0]
]

for l,s in test_lists:
    print(deep_add(l,s))