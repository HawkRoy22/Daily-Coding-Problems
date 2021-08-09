

def replaceElements(arr):
    fin =[]
    for x in arr[:len(arr) - 1]:
        temp = arr[arr.index(x) + 1:]
        tempMax = max(temp)
        fin.append(tempMax)
    fin.append(-1)

    arr = fin

    print(arr)


replaceElements([17, 18, 5, 4, 6, 1])
replaceElements([400])
replaceElements([2,3,5,52,1,23,4])
replaceElements([56903,18666,60499,57517,26961])

