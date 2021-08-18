#Given two binary strings a and b, return their sum as a binary string.



def addBinary(a, b):
    y = int(a, 2)
    b = int(b, 2)
    temp = y + b
    answer = bin(temp).replace("0b", "")
    return answer


addBinary('11','1')