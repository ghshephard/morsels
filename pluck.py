sentinel=object()

def pluck(indic, *keys, sep=".", default=sentinel):
    def _pluck(indic, key, sep, default):
        try:
            if sep in key:
                head = key.split(sep)[0]
                tail = sep.join(key.split(sep)[1:])
                return _pluck(indic[head], tail, sep=sep, default=default)
            else:
                return indic[key]
        except KeyError:
            if default != sentinel:
                return default
            else:
                raise
    if len(keys) > 1:     
        return tuple(_pluck(indic, key, sep, default) for key in keys)
    else:
        print(indic,keys,sep,default)
        return _pluck(indic,keys[0],sep,default)      
            
            
            
    