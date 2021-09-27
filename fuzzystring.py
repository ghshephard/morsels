from functools import total_ordering

@total_ordering
class FuzzyString(str):
    def __init__(self, intext):
        self.intext = intext

    def __eq__(self, other):
        return self.intext.lower() == other.lower()

    def __lt__(self, other):
        return self.intext.lower() < other.lower()

    # def __ne__(self, other):
    #     return not self.intext == other
        

a=FuzzyString('abc')
b=FuzzyString('bcd')

print(a > b)
# greeting = FuzzyString('Hey TREY!')
# assert (greeting == 'hey Trey!') == True
# assert ( greeting == 'heyTrey') == False
# assert ( greeting != 'heyTrey') == True

