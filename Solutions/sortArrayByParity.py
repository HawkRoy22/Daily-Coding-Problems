#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.



def sortArrayByParity(nums):
    e = []
    o = []
    for x in nums:
        if x % 2 == 0:
            e.append(x)
        else:
            o.append(x)
    nums = e + o

    print(nums)

sortArrayByParity([3,1,4,2])