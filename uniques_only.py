def uniques_only(incoming):
    chkset = set()
    for i in incoming:
        if i not in chkset:
            yield i
    chkset.add(i)


if __name__ == "__main__":
    nums = [1, -3, 2, 3, -1]
    squares = (n**2 for n in nums)
    chklst = [
        [1, 2, 2, 1, 1, 3, 2, 1],
        [squares]
        ]
    for chk in chklst:
        print(list(uniques_only(chk)))
