
# Validate Parentheses

def isValid(s):

    stack = []

    checker = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }

    # Check 1: If the length of the string is odd, then it is automatically invalid
    if len(s) % 2 != 0: 
        return False

    # Logic, first half goes in the stack, then the second half should check the dictionary for 
    for j in s:
        if j in checker:
            if stack and stack[-1] == checker[j]:
                stack.pop()
            else:
                return False
        else:
            stack.append(j)
    
    if len(stack) != 0:
        return False
    return True
    
isValid("(([{(())}]))")
isValid("(")