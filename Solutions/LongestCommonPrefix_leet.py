#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

from collections import Counter

from collections import Counter


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        # if size is 0, return empty string
        if (size == 0):
            return ""

        if (size == 1):
            return strs[0]

        # sort the array of strings
        strs.sort()

        # find the minimum length from
        # first and last string
        end = min(len(strs[0]), len(strs[size - 1]))

        # find the common prefix between
        # the first and last string
        i = 0
        while (i < end and
               strs[0][i] == strs[size - 1][i]):
            i += 1

        pre = strs[0][0: i]
        return pre


def average(strs):
    sum = 0
    for x in strs:
        sum += len(x)
    avg = sum // len(strs)
    return avg


longestCommonPrefix(["flower", "flow", "flight"])#fl
#average(["flower", "flow", "flight"])
longestCommonPrefix(["dog","racecar","car"])# NONE
longestCommonPrefix(["ab","a"]) # a
longestCommonPrefix(["a"])# a
longestCommonPrefix([""])# NONE


#First Attempt

#fin = ""
#duh = ""
#yuh = ""

#ahah = average(strs)

#if ahah >= 3:
#    for x in strs:
#        duh += x[:len(x) // 2]
#    c = Counter(duh)
#    for keys, values in c.items():
#        if values == len(strs):
#            fin += keys
#    print(fin)
#elif ahah < 3:
#    for z in strs:
#        yuh += z
#    d = Counter(yuh)
#    for keys, values in d.items():
#        if values == len(strs):
#            fin += keys
#    print(fin)
#else:
#    print("nah")