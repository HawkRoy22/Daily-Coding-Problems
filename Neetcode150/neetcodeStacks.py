
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
            print("inside")
            
        
    
is