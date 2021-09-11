import math



def mySqrt(x):
    fin = []
    if x == 1:
        return x
    for j in range(2, x//2):
        temp = j * j
        if temp <= x:
            fin.append(j)
    if len(fin) == 0:
        return 0
    else:
        return (fin[-1])




mySqrt(16)
mySqrt(8)
mySqrt(4)

