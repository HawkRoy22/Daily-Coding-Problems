#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.



def searchInsert(nums, target):
    fin = nums
    fin.append(target)
    fin.sort(reverse=False)
    if target in nums:
        print(nums.index(target))
    else:
        print(fin.index(target))


searchInsert([1,3,5,6], 5)
searchInsert([1,3,5,6], 7)