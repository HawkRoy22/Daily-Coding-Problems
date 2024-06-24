
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
    
#isValid("(([{(())}]))")
#isValid("(")


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        print(self.stack)
        self.stack.insert(0,val)
        print(self.stack)

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return min(self.stack)

# Evaluate Reverse Polish Notation



def evalRPN(tokens):
    """"You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
        Return the integer that represents the evaluation of the expression.

        The operands may be integers or the results of other operations.
        The operators include '+', '-', '*', and '/'.
        Assume that division between integers always truncates toward zero."""
    fin = 0 
    stack = []
    operators = ['+', '-', '*', '/']

    for j in tokens:
        if j not in operators:
            stack.append(j)
            #stack.insert(0, j)
        else:
            match j:
                case '+':
                    fin += stack[0] + stack[1]
                    stack.clear()
                case '-':
                    fin += stack[0] - stack[1]
                    stack.clear()
                case '*':
                    fin += stack[0] * stack[1]
                    stack.clear()
                case '/':
                    fin += stack[0] / stack[1]
                    stack.clear()
