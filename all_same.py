def all_same(seq):
    allset = set()
    for item in seq:
        allset.add(repr(item))
        if len(allset) > 1:
            return False
    else:
        return True
        

if __name__ == "__main__":
    assert all_same([1, 1, 1]) 
    assert not  all_same([1, 0, 1])
    assert all_same([(1, 'a'), (1, 'a')])
    assert not all_same([(1, 'a'), (1, 'b')])