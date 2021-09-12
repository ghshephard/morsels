
class EasyDict(dict):
    def _norm(self, k):
        if self.normalize:
            return k.replace(" ","_")
        else:
            return k

    def _normdic(self, dic):
        return {self._norm(k):v for k,v in dic.items()}

    def __init__(self, *args, normalize = False, **kwargs):
        self.normalize=normalize
        args = ( self._normdic(item ) if isinstance(item, dict) else item for item in args)
        kwargs = self._normdic(kwargs)
        self.__dict__.update(*args, **kwargs)

    def __getitem__(self, key):
        return self.__dict__[self._norm(key)]

    def __setitem__(self, key, value):
        self.__dict__[self._norm(key)] = value

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if self.__dict__ == other.__dict__:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__dict__ != other.__dict__:
            return True
        else:
            return False
    def get(self, key, default = None):
        return self.__dict__.get(self._norm(key),default)
        

if __name__ == "__main__":
    person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
    assert person.name == 'Trey Hunner'
    person.location = "Portland"
    assert person['location'] == 'Portland'
    person['location'] = "San Diego"
    assert person.location == 'San Diego'
    person = EasyDict(name="Trey Hunner", location="San Diego")
    assert person.location == 'San Diego'
    assert (person == EasyDict(name="Trey", location="San Diego")) == False
    assert (person != EasyDict(name="Gordon")) == True
    assert (person == EasyDict(name="Trey Hunner", location="San Diego")) == True
    assert person.get('profession') == None
    assert person.get('profession', 'unknown') == "unknown"
    assert person.get('name', 'unknown') == 'Trey Hunner'
    person = EasyDict(name="Trey Hunner", location="San Diego", normalize=True)
    person['company name'] = "Truthful Technology LLC"
    assert person.company_name == "Truthful Technology LLC"
    assert person['company name'] == "Truthful Technology LLC"
    person = EasyDict({'name':'Gordon Shephard', 'first job':'Mcdonalds'}, normalize=True)
    assert person.first_job == 'Mcdonalds'
