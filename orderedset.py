class OrderedSet:
    def __init__(self, items=[]):
        self._myset={}
        for i in items:
            if not(i in self._myset):
                self._myset[i]=True

    def __iter__(self):
        return iter(self._myset.keys())

    def __len__(self):
        return len(self._myset.keys())

    def __repr__(self):
        return(str(self.__class__.__name__))+"("+str(list(self))+")"
    
    def __contains__(self,item):
        return item in self._myset.keys()
    

def main():
    ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
    assert(list(OrderedSet(ordered_words))) == ['these', 'are', 'words', 'in', 'an', 'order']
    print("All Tests Passed")



if __name__=="__main__":
    main()