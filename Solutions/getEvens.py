#Given an array nums of integers, return how many of them contain an even number of digits.


def findEven(nums):
    evens = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            evens += 1

    return evens

findEven([555,901,482,1771])