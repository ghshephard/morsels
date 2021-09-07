from collections import UserDict

class PermaDict(UserDict):
    def __init__(self, *args,silent=False, **kwargs):
        self.silent=silent
        super().__init__(*args, **kwargs)
        
    def __setitem__(self, key, value):
        if not key in self:
            super().__setitem__(key,value)
        elif not self.silent:
            raise KeyError(f"{key} already in dictionary.")
        
    def update(self, *args, force=False, **kwargs):
        if not force:
            super().update(*args, **kwargs)
        else:
            self.data.update(*args, **kwargs)
        
    def force_set(self, key,value):
        super().__setitem__(key,value)

if __name__ == "__main__":
    p=PermaDict({'a':1,'b':2})
    try:
        p.update({'a':3})
    except KeyError as e:
        print (f"Passed: {e}")
    print(p)
