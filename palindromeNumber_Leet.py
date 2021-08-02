

#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        bruh = len(temp) // 2
        first = temp[:bruh]
        last = temp[bruh+1:]
        lastss = temp[bruh:]
        if 0 <= x <= 9:
            return True
        if len(temp) % 2 == 0:
            if first == lastss[::-1]:
                return True
        elif first == last[::-1]:
            return True
        else:
            return False



isPalindrome(1234321)
isPalindrome(122)
isPalindrome(9012109)
isPalindrome(0)
isPalindrome(11)
isPalindrome(1001)
