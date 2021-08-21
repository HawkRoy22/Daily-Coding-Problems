def tribonacci(signature,n):
    z = 0
    if n == 0:
        return []
    if n < 3:
        return signature[:n]


    while len(signature) < n:
        signature.append(sum(signature[z:z+3]))
        z += 1
    print(signature)

#tribonacci([1, 1, 1], 10)
