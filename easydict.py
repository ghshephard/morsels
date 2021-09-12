class EasyDict(dict):
    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)
    def __getitem__(self, key):
        return self.__dict__[key]
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __repr__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        if self.__dict__ == other.__dict__:
            return True
        else:
            return False
        

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
    assert (person == EasyDict(name="Trey Hunner", location="San Diego")) == True
