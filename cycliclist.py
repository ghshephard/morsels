class CyclicList:
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __iter__(self):
        while True:
            for element in self.iterable:
                yield element

    def __len__(self):
        return len(self.iterable)

    def append(self, i):
        self.iterable.append(i)

    def pop(self, i=-1):
        return self.iterable.pop(i)

    def _gindex(self,i):
        if i < 0:
            point = (len(self.iterable) - (abs(i) % len(self.iterable) ) ) % len(self.iterable)
        else:
            point = i % len(self.iterable)
        return point

    def __getitem__(self,subsc):
        if isinstance(subsc, slice):
            lst=[]
            start, stop = subsc.start, subsc.stop
            if  start is None:
                start = 0
            if stop is None:
                stop = len(self.iterable) if start >= 0 else 0
            if stop - start == 0:
                lst=[]
            else:
                for i in range(start, stop):
                    lst.append(self.iterable[self._gindex(i)])
            return lst
        else:
            return self.iterable[self._gindex(subsc)]

    def __setitem__(self, i, val):
        self.iterable[self._gindex(i)] = val


    

if __name__ == "__main__":
    from itertools import islice
    my_list = CyclicList([1, 2, 3])
    assert list(islice(my_list, 5)) == [1,2,3,1,2]
    my_list = CyclicList([1])
    assert list(islice(my_list, 5)) == [1,1,1,1,1]
    my_list = CyclicList(range(4))
    assert list(islice(my_list, 5)) == [0,1,2,3,0]
    my_list = CyclicList("GORD")
    assert list(islice(my_list, 5)) == ["G","O","R","D","G"]
    my_list = CyclicList((x for x in [1,2,3]))
    assert(list(islice(my_list,5))) == [1,2,3,1,2]
    my_list = CyclicList([1, 2, 3])
    my_list.append(4)
    assert(my_list.pop()) == 4
    assert len(my_list) == 3
    assert my_list.pop(0) == 1
    assert len(my_list) == 2
    my_list = CyclicList([1, 2, 3])
    assert my_list[1] == 2
    assert my_list[-1] == 3
    assert my_list[5] == 3
    assert my_list[-4] == 3
    my_list = CyclicList([1, 2, 3])
    my_list[0] = 99
    assert my_list[-3] == 99
    my_list = CyclicList([1, 2, 3])
    assert my_list[-2:] == [2, 3]
    assert my_list[:8] == [1, 2, 3, 1, 2, 3, 1, 2]
    assert my_list[-2:2] == [2, 3, 1, 2]
    assert my_list[:-1] == []
    numbers = CyclicList([1, 2, 3, 4, 5])
    assert numbers[:7] == [1, 2, 3, 4, 5, 1, 2]
