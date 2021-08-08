def removeDuplicates(nums):
    N = len(nums)
    fin = []
    #Sorting the array out
    nums.sort(reverse=False)

    for x in range(N-1):
        if nums[x+1] == nums[x]:
            fin.append(nums[x+1])

    for j in fin:
        nums.remove(j)

    print(nums)

removeDuplicates([2, 1, 1])
removeDuplicates([2,2,2,1,4])