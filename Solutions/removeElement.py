

def remove(nums, val):
    tin = []
    for x in nums:
        if x == val:
            tin.append(x)

    for j in tin:
        nums.remove(j)

    print(nums)

remove([0,1,2,2,3,0,4,2], 2)