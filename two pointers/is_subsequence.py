"""
392. Is Subsequence

Given two strings s and t,
return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed
from the original string by deleting some (can be none)
of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).



Example 1:
>>> Solution().isSubsequence(s = "abc", t = "ahbgdc")
True

Example 2:

>>> Solution().isSubsequence(s = "axc", t = "ahbgdc")
False

>>> Solution().isSubsequence(s = "", t = "ahbgdc")
True

>>> Solution().isSubsequence(s = "b", t = "ahbgdc")
True
"""

import doctest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first, second = 0, 0

        while second < len(t) and first < len(s):
            if s[first] == t[second]:
                first += 1
                second += 1
            else:
                second += 1
        if first == len(s):
            return True
        else:
            return False


doctest.testmod()
