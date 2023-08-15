class OrderedSet:
    def __init__(self, items):
        self._myset={}
        for i in items:
            if not(i in self._myset):
                self._myset[i]=True

    def __iter__(self):
        return iter(self._myset.keys())
    
    

    