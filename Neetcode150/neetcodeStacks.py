
# Validate Parentheses

import math


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
    sumOf = 0

    stack = []
    
    for j in tokens:
        if j.lstrip('-').isdigit():
            stack.append(int(j))
        else:
            if j == '+':
                sumOf = stack[-1] + stack[-2]
            elif j == '-':
                sumOf =stack[-1]- stack[-2]
            elif j == '*':
                sumOf = stack[-2] * stack[-1]
            elif j == '/':
                sumOf = int((stack[-2] / stack[-1]))

            stack.pop()
            stack.pop()
            stack.append(sumOf)
            print("Stack : ", stack)


    print(stack[0])

    return stack[0]

#evalRPN(["2","1","+","3","*"])
#evalRPN(["4","13","5","/","+"])

#evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])



def dailyTemperatures(temperatures):
    result = []
    l = 0 
    r = 1
    counter = 0

    while l < len(temperatures):

        if r >= len(temperatures):
            l += 1
            r = l + 1
            counter = 0
            result.append(counter)

        elif temperatures[r] > temperatures[l]:
            counter += 1
            result.append(counter)
            counter = 0 
            l += 1
            r = l + 1
        else:
            counter += 1
            r += 1
    
    print(result)

#dailyTemperatures([30,38,30,36,35,40,2])
#dailyTemperatures([22,21,20])
dailyTemperatures([55,38,53,81,61,93,97,32,43,78])


