

def heightChecker(nums):
    fin = sorted(nums)
    counter = 0
    zipo = zip(nums, fin)
    for x, y in zipo:
        if x != y:
            counter += 1

    print(counter)



heightChecker([1,1,4,2,1,3])
heightChecker([1,2,3,4,5])
heightChecker([5,1,2,3,4])


