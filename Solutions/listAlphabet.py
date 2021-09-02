def listAlphabet(n):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    fin = []
    for i in range(len(n)):
        if n[i].islower():
            fin.append(str(lower.index(n[i])+1))
        elif n[i].isupper():
            fin.append(str(upper.index(n[i])+1))
    print(fin)
    print(" ".join(fin))
