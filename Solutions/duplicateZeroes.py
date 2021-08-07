def duplicateZeros(arr):
    leng = len(arr)
    tin = []
    for i in range(len(arr)):
        if arr[i] == 0:
            tin.append(i)

    for j in tin[::-1]:
        arr.insert(j+1, 0)

    del arr[leng:]
    print(arr)

duplicateZeros([1,0,2,3,0,4,5,0])
duplicateZeros([0,1,7,6,0,2,0,7])