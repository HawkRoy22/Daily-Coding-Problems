

def isValid(s):
    round = []
    square = []
    curly = []

    for j in s:
        if j == '(':
            round.append(j)
        if j == '[':
            square.append(j)
        if j == "{":
            curly.append(j)
        if j == ')':
            try:
                round.pop()
            except:
                print(False)
        if j == ']':
            try:
                square.pop()
            except:
                print(False)
        if j == '}':
            try:
                curly.pop()
            except:
                print(False)

    if len(curly) == len(square) == len(round):
        print(True)
    else:
        print(False)


#isValid("()")#true
#isValid("()[]{}")#true
#isValid("(]")#false
#isValid("([)]")#false
#isValid("{[]}")#true


def yuh(s):
    ahh = []
    first = []
    last = []

    for j in s:
        if j == '(':
            ahh.append(1)
        if j == '[':
            ahh.append(2)
        if j == '{':
            ahh.append(3)
        if j == ')':
            ahh.append(-1)
        if j == ']':
            ahh.append(-2)
        if j == '}':
            ahh.append(-3)

    for x in ahh:
        if x > 0:
            first.append(x)
        else:
            last.append(x)


    last = [-x for x in last]
    last.reverse()



    if sum(ahh) == 0:
        if first == last:
            print(True)
        elif:
        else:
            print(False)
    else:
        print(False)



yuh("([)]")#False
yuh("(]")#False
yuh("{[]}")#True
yuh("(){}}{")#False
yuh("()[]{}")#True

