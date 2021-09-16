from collections.abc import Mapping

class ProxyDict(Mapping):
    def __init__(self, d={}):
        self._d = d
        #super().__init__()
    def __getitem__(self, k):
        return self._d[k]
    def __len__(self):
        return len(self._d)
    def __iter__(self):
        return iter(self._d)
    def __repr__(self):
        return f'{type(self).__name__}({self._d})'


if __name__ == "__main__":
    user_data = {'name': 'Trey Hunner', 'active': False}
    proxy_data = ProxyDict(user_data)
    print(list(proxy_data.keys()))
    print(proxy_data['name'])
    print(proxy_data['active'])
    try:
        proxy_data['active'] = False
    except TypeError:
        print("Success.  Exception on set value.") 

