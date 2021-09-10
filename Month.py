from functools import total_ordering
from calendar import monthrange
import datetime
@total_ordering

class Month:
    def __init__(self,year,month):
        self.year = year
        self.month = month
        self.first_day = datetime.date(self.year, self.month, 1)
        weeks, days = monthrange(year, month)
        self.last_day = datetime.date(self.year, self.month, days)

    def _is_valid_operand(self, other):
        if not hasattr(other,"year") or not hasattr(other,"month"):
            return False
        else:
            return True
 
    def __eq__(self,other):
        if not self._is_valid_operand(other):
            return False
        else:
            return self.__repr__() == other.__repr__()
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            raise TypeError
        return( (self.year, self.month) < (other.year, other.month))
    def __repr__(self):
        return(f'{type(self).__name__}({self.year},{self.month})')

    def __str__(self):
        return(f'{self.year:04}-{self.month:02}')
    @classmethod
    def from_date(self,dt):
        year, month, day, *_ = datetime.date.timetuple(dt)
        return Month(year, month)


if __name__ == "__main__":
    dec99 = Month(1999, 12)
    jan01=Month(2001,1)
    print(dec99)
    print(jan01)
    print( sorted([Month(1998, 12), Month(2000, 1), Month(1999, 12)]))
    m1=Month(1998, 12)
    m2=Month(1998,12)
    print
    print(f"Equality - {m1} == {m2} {m1 == m2} ")
    t1=(1998,12)
    print(f"({m1} == {t1}) {m1 == t1}")
    try:
        print(m1 < t1)
    except TypeError:
        print(f"Success - TypeError on {m1} < {t1}")
    dec99 = Month(1999, 12)
    print(f'First day of {dec99} is {dec99.first_day}')
    print(f'Last day of {dec99} is {dec99.last_day}')
    nye99 = datetime.date(1999, 12, 31)
    dec99 = Month.from_date(nye99)
    print(f"Month from {nye99} is {dec99}")


    
