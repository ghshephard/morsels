"""Dictools for pymorsels"""
def pluck(indic, search, sep="."):
    """Search a dictionary on search and return value"""
    keys = search.split(sep)
    return indic[keys[0]] if len(keys)==1 else pluck(indic[keys[0]], ".".join(keys[1:]))


def main():
    """main"""
    data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
    assert(pluck(data, 'amount')) == 10.64
    assert(pluck(data, 'category.group')) == "Fun"
    data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
    assert(pluck(data, 'category/name', sep='/') == "Music")
    print("All Tests Passed!")

if __name__ == "__main__":
    main()
