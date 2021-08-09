

def moveZeroes(nums):
    for x in nums:
        if x == 0:
            t = nums.pop(nums.index(x))
            nums.append(t)

    print(nums)

moveZeroes([0,1,0,3,12])