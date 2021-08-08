from itertools import combinations

def checkIfExist(arr):
    arr.sort(reverse=True)
    fin = []
    for i, j in combinations(arr, 2):
        if i == j * 2 or i * 2 == j:
            fin.append(j)

    if len(fin) > 0:
        print(True)
    else:
        print(False)


checkIfExist([10, 2, 5, 3])
checkIfExist([7, 1, 14, 11])
checkIfExist([3, 1, 7, 11])
checkIfExist([-2,0,10,-19,4,6,-8])
checkIfExist([0,0])