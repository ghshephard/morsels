from math import ceil

class float_range:
    def __init__(self,start, stop=None, step=1):
        if  stop is None:
            self.start=0
            self.stop=start
        else:    
            self.start = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        cur = self.start
        if ( (self.start < self.stop and self.step <=0)  or
              (self.start > self.stop and self.step >=0) ):
              pass
        else:
            if self.start < self.stop:
                while cur < self.stop:
                    yield cur
                    cur += self.step 
            else:
                while cur > self.stop:
                    yield cur
                    cur += self.step 

            
    def __len__(self):
        return abs(ceil((self.stop - self.start ) / self.step))


fr = float_range(5,0,-1)

print(len(fr))
print(list(fr))
