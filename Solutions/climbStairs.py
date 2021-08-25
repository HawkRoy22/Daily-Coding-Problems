
class Solution:
    cache = {}
    def climbStairs(self, n):
        if n < 3:
            return n
        else:
            return self.other( n -1) + self.other( n -2)

    def other(self, n):
        if n not in self.cache.keys():
            self.cache[n] = self.climbStairs(n)
        return self.cache[n]




climbStairs(3)
climbStairs(8)



