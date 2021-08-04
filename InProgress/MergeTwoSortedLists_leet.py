
#Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

def mergeTwoLists(l1, l2):
    fin = []
    for x, y in zip(l1, l2):
        fin.append(x)
        fin.append(y)

    for i in range(1, len(fin)):
        key = fin[i]
        j = i - 1
        while j >= 0 and key < fin[j]:
            fin[j+1] = fin[j]
            j -= 1
        fin[j+1] = key

    print(fin)


mergeTwoLists([1,2,4],[3, 1,4])
