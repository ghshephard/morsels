from collections import Counter

def format_ranges(numbers):
    def getnum(lst, index):
        num,c = lst[index]
        if c > 1:
            lst[index]=(num,c-1)
            index += 1
        else:
            lst.pop(index)
        if index >= len(lst):
            index = 0 
        return index, num

    lst = sorted(Counter(numbers).items())
    index = 0

    index, num = getnum(lst, index)
    first = current = num
    nums = []
    while lst:
        index, num  = getnum(lst, index)
        if num != current + 1:
            nums.append((first, current))
            first = num 
        current = num

    nums.append((first, current))
    srtnums = sorted(nums, key = lambda x:(x[0],x[1]-x[0]))
    ret = ",".join( f'{a}-{b}' if b>a else f'{a}' for (a,b) in srtnums )    
    return ret

if __name__ == "__main__":
    assert (format_ranges([1, 2, 3, 4, 5, 6, 7, 8])) == '1-8'
    assert (format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])) =='1-3,5-8,10-11'
    numbers = [3, 4, 15, 16, 17, 19, 20]
    assert (format_ranges(n+1 for n in numbers)) == '4-5,16-18,20-21'
    assert(format_ranges([4] )) == '4'
    assert(format_ranges([1, 3, 5, 6, 8])) == '1,3,5-6,8'
    assert(format_ranges([9, 1, 7, 3, 2, 6, 8]) == "1-3,6-9")
    assert(format_ranges([1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7])) == '1-2,1-4,4,7,7-9'
    assert(format_ranges([1, 3, 5, 6, 8])) == '1,3,5-6,8'

