
def thirdMax(nums):
    num = list(set(nums))
    if len(num) < 3:
        return max(num)

    fin = []
    x = 0
    while x < 3:
        t = max(num)
        fin.append(t)
        num.pop(num.index(t))
        x += 1

    return min(fin)






thirdMax([3,2,1])
thirdMax([1,2])
thirdMax([2,2,3,1])
