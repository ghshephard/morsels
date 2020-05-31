import math

class float_range:
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        if step is None:
            self.step = 1.0
        else:
            self.step = step

    def _done(self, cur, start, stop, step):
        if start < stop and cur < stop:
            if step > 0:
                return False
            else:
                return True
        elif start > stop and cur > stop:
            if self.step < 0:
                return False
            else:
                return True
        else:
            return True

    def __len__(self):

        len = math.floor((self.stop - self.start) / self.step) + 1
        if len >= 0:
            return len
        else:
            return 0

    def __iter__(self):
        cur = self.start
        while not self._done(cur, self.start, self.stop, self.step):
            yield cur
            cur += self.step


if __name__ == "__main__":
    tstcon = (
        (0.5, 2.5, 0.5),
        (3.5, 0, -1),
        (0.0, 3.0, None),
        (3.0, None, None),
        (5, 10, 1.5),
        (10, 5, 1.5),
        (10, 5, -1.5),
        (5, 10, -1.5),
    )
    for start, stop, end in tstcon:
        fr = float_range(start, stop, end)
        print( [start,stop,end], len(fr),list(fr))
