def get_earliest(*dates):
    def _dkey(dt):
        m,d,y = dt.split("/")
        return (y,m,d)

    return min (dates, key = _dkey)

if __name__ == "__main__":
     print(get_earliest("02/24/1946", "01/29/1946", "03/29/1945"))