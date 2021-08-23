def dirReduc(arr):
    z = collections.defaultdict(int)
    for c in arr:
        z[c] += 1
    ayo = []
    yah = []
    for a in z.items():
        if a[0] == 'NORTH' or a[0] == 'SOUTH':
            ayo.append(a)
        else:
            yah.append(a)
    if ayo[0][1] == ayo [1][1]:
        vert = True
    else:
        pass

    print(z)
    print(ayo)
    print(yah)
    print(vert)


#dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])

#duplicate_count('abcdeaa')
#duplicate_count('abcdeaB')
#duplicate_count("Indivisibilities")