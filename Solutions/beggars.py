def beggars(values, n):
    # your code here
    temp = str(values)
    total = 0
    for x in values: total += x
    if(n>1):
        act = temp.split(',')

    else:
        print(total)