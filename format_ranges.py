def format_ranges(numbers):
    lst=[]
    iterator = iter(numbers)
    first = current = next(iterator)
    for i in iterator:
        if i > current + 1:
            lst.append( (first,current))
            first = i
        current = i
    lst.append( ( first, current ))
    ret = ",".join( f'{a}-{b}'  for (a,b) in lst )    
    return ret


if __name__ == "__main__":
    assert (format_ranges([1, 2, 3, 4, 5, 6, 7, 8])) == '1-8'
    assert (format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])) =='1-3,5-8,10-11'
    numbers = [3, 4, 15, 16, 17, 19, 20]
    assert (format_ranges(n+1 for n in numbers)) == '4-5,16-18,20-21'


