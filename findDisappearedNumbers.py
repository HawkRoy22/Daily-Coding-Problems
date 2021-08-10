

def findDisappearedNumbers(nums):
    fin = []
    counter = 1
    for x in range(len(nums)):
        fin.append(counter)
        counter += 1

    duh = list(set(fin) - set(nums))
    return duh

findDisappearedNumbers([4,3,2,7,8,2,3,1])