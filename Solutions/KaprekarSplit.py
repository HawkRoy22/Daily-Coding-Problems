def kaprekar_split(n):
    squared = n * n
    sqList = [str(x) for x in str(squared)]
    half = len(sqList) // 2
    first = sqList[:half]
    second = sqList[half:]

    fi = ''
    si = ''

    for i in first:
        fi += i
    if fi != '':
        fi = int(fi)
    else:
        fi = 0

    for j in second:
        si += j
    if si != '':
        si = int(si)
    else:
        si = 0