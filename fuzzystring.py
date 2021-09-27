import unicodedata

class FuzzyString(str):

    def _nc(self, text):
        return unicodedata.normalize("NFKD", text.casefold())

    def __init__(self, intext):
        self.intext = intext
    def __eq__(self, other):
        return self._nc(self.intext.lower()) == self._nc(other.lower())
    def __ne__(self,other):
        return self.intext.lower() != other.lower()
    def __lt__(self, other):
        return self.intext.lower() < other.lower()
    def __gt__(self,other):
        return self.intext.lower() > other.lower()
    def __ge__(self,other):
        
        return self.intext.lower() >= other.lower()
    def __le__(self,other):
        return self.intext.lower() <= other.lower()
    def __contains__(self, other):
        return self._nc(other.lower()) in self._nc(self.intext.lower())
    def __add__(self, other):
        return FuzzyString("".join([self.lower(),other]))
        
        


a=FuzzyString('abc')
b=FuzzyString('BCD')

greeting = FuzzyString('Hey TREY!')
assert (greeting == 'hey Trey!') == True
assert ( greeting == 'heyTrey') == False
assert ( greeting != 'heyTrey') == True
o_word = FuzzyString('Octothorpe')
assert ('hashtag' < o_word) == True
assert ('hashtag' > o_word) == False
tokyo = FuzzyString("tokyo")
toronto = FuzzyString("TORONTO")
assert (tokyo < toronto) == True
assert (toronto < tokyo) == False
apple = FuzzyString('Apple')
assert  (apple >= "animal")
ss = FuzzyString('ss')
assert('\u00df' == ss)
e = FuzzyString('\u00e9')
assert('\u0065\u0301' == e)
assert('\u0301' in e)