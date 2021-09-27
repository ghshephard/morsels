class FuzzyString(str):
    def __init__(self, intext):
        self.intext = intext
    def __eq__(self, other):
        return self.intext.lower() == other.lower()
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