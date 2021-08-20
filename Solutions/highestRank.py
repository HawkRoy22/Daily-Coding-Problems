def highest_rank(arr):
    theCount = collections.Counter(arr)
    theKeys = []
    temp = 0
    fin = []
    for key in theCount.items():
        theKeys.append(key[1])
    for j in range(len(theKeys)):
        if theKeys[j] > temp:
            temp = theKeys[j]
    for number, count in theCount.items():
        if count == temp:
            fin.append(number)
    print(max(fin))

#highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12])
#highest_rank([12, 10, 8, 12, 7, 8, 4, 8, 12])