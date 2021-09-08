from itertools import zip_longest

FILLVALUE=object()

def interleave(*args):
    for r in zip_longest(*args, fillvalue = FILLVALUE):
        for c in r:
            if c is not FILLVALUE:
                yield c

if __name__ == "__main__":
    print(list(interleave([1,2,3,4],[5,6,7,8])))
    nums = [1,2,3,4]
    print(list(interleave(nums, (n**2 for n in nums))))
    print(list(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])))
    print(list(interleave([1, 2, 3], [4, 5, 6, 7, 8])))
    print(list(interleave([1, 2, 3], [4, 5], [6, 7, 8, 9])))