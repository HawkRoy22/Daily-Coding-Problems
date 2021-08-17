#Given an integer array nums, find the contiguous subarray containing at least one
#number) which has the largest sum and return its sum.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        current_largest_sum = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
            if dp[i] > current_largest_sum:
                current_largest_sum = dp[i]
        return current_largest_sum


maximumSubarray([-2,1,-3,4,-1,2,1,-5,4])#6
maximumSubarray([1])#1
maximumSubarray([5,4,-1,7,8])#23
maximumSubarray([-1])#-1
maximumSubarray([-2,1])#1

#PAST ANSWERS __ TAKES TOO LONG

def maximum(nums):
    suma = sum(nums)
    for x in range(len(nums)):
        for j in range(len(nums)):
            temp = nums[x:j + 1]
            if sum(temp) > suma and len(temp) != 0:
                suma = sum(temp)
    print(suma)


def maximumSub(nums):
    theMax = nums[0]
    for i in range(len(nums) + 1):
        for j in range(i):
            if theMax < sum(nums[j: i])
    print(max(fin))
