def diamond(n):
    tt = []
    for num in range(1, n+1):
        if num % 2 != 0:
            tt.append(num)
    if n % 2 == 0:
        print(None)
    else:
        mid = n / 2 + 1
        for x in tt:
            print(x * '*')
        tt.reverse()
        tt.remove(tt[0])
        for z in tt:
            print(z * '*')
            print("\n")
