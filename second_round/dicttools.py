"""Dictools for pymorsels"""
SENTINEL=object()

def pluck(indic, search, sep=".", default=SENTINEL):
    """Search a dictionary on search and return value"""
    keys = search.split(sep)
    if default==SENTINEL:
        return indic[keys[0]] if len(keys)==1 else pluck(indic[keys[0]], ".".join(keys[1:]))
    else:
        try:
            return indic[keys[0]] if len(keys)==1 else pluck(indic[keys[0]], ".".join(keys[1:]))
        except KeyError:
            return default


def main():
    """main"""
    data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
    assert(pluck(data, 'amount')) == 10.64
    assert(pluck(data, 'category.group')) == "Fun"
    data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
    assert(pluck(data, 'category/name', sep='/')) == "Music"
    data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
    assert(pluck(data, 'category.created', default='N/A')) == "N/A"
    print("All Tests Passed!")

if __name__ == "__main__":
    main()
