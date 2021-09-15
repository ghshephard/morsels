def chunked(sequence, n):
     for i in range(0,len(sequence),n):
         yield list(sequence[i:i+n])

if __name__ == "__main__":
    for chunk in chunked([1,2,3,4,5],n=2):
        print(*chunk)
    for chunk in chunked(range(10), 4):
        print(tuple(chunk))
    # squares = (n**2 for n in range(6))
    # for chunk in chunked(squares, 3):
    #     print(*chunk)