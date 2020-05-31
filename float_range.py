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

    def __iter__(self):
        cur = self.start
        while not self._done(cur, self.start, self.stop):
            yield cur
            cur += self.step

    def _done(self, cur, start, stop):
        if start < stop and cur < stop:
            return False
        elif start > stop and cur > stop:
            return False
        else:
            return True


if __name__ == "__main__":
    tstcon = (
        (0.5, 2.5, 0.5),
        (3.5, 0, -1),
        (0.0, 3.0, None),
        (3.0, None, None,)
    )
    for start, stop, end in tstcon:
        fr = float_range(start, stop, end)
        print(list(fr))
