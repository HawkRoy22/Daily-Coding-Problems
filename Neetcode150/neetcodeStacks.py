

def isValid(s):

    checker = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = []

        for j in s:
            if j not in stack:
                stack.append(j)