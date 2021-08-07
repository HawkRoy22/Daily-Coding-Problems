def thelargest(nums):
    fin = ""
    for x in nums:
        fin += str(x)

    yuh = fin.split('0')
    ans = []
    for i in yuh:
        ans.append(len(i))

    print(max(ans))







thelargest([1, 1, 0, 1, 1, 1])