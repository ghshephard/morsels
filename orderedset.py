class OrderedSet:
    def __init__(self, items=[]):
        self._myset={}
        for i in items:
            self.add(i)

    def __iter__(self):
        return iter(self._myset.keys())

    def __len__(self):
        return len(self._myset.keys())

    def __repr__(self):
        return(str(self.__class__.__name__))+"("+str(list(self))+")"
    
    def __contains__(self,item):
        return item in self._myset.keys()
    
    def __eq__(self, other):
        if isinstance(other,OrderedSet) and list(self._myset.keys()) == list(other):
            return True
        elif isinstance(other,set) and set(self._myset.keys()) == set(other):
            return True
        else:
            return False
    def add(self,item):
        if not(item in self._myset):
            self._myset[item]=True

    def discard(self, item):
        try:
            self._myset.pop(item)
        except KeyError:
            pass


def main():
    ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
    assert(list(OrderedSet(ordered_words))) == ['these', 'are', 'words', 'in', 'an', 'order']
    s2=OrderedSet([5,2,1,4,3])
    s2.add(7)
    assert(list(s2))==[5,2,1,4,3,7]
    s2.discard(5)
    assert(list(s2)==[2,1,4,3,7])
    print("All Tests Passed")



if __name__=="__main__":
    main()