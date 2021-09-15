NOTHING = object()
def chunked(sequence, n, *, fill=NOTHING):
    iterator=iter(sequence)
    
    try:
        while iterator:
            ret = []
            for i in range(n):
                ret.append(next(iterator))
            yield ret
    except StopIteration:
        if ret:
            yield ret+[fill]*(n-len(ret)) if fill is not NOTHING else ret 
 
    
if __name__ == "__main__":
    for chunk in chunked([1,2,3,4,5],n=2):
        print(*chunk)
    for chunk in chunked(range(10), 4):
        print(tuple(chunk))
    squares = (n**2 for n in range(6))
    for chunk in chunked(squares, 3):
        print(*chunk)
    for chunk in chunked(range(10), 4, fill=0):
        print(*chunk)

    for chunk in chunked(range(4), 2, fill=0):
        print(*chunk)
