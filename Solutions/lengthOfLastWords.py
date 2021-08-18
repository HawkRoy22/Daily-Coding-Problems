#Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.


def lengthOfLastWord(s):
    fin = " ".join(s.split())
    fin = fin.split(" ")
    print(len(fin[len(fin)-1]))


lengthOfLastWord("Hello      World")
lengthOfLastWord("   fly me   to   the moon  ")
lengthOfLastWord("luffy is still joyboy")
