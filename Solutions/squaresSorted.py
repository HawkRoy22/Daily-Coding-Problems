#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



def squareSorted(nums):
    fin = []
    for i in nums:
        fin.append(i**2)

    fin.sort(reverse=False)
    print(fin)

squareSorted([-4,-1,0,3,10])