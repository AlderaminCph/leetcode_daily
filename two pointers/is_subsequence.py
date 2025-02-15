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
"""

import doctest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        second = 0
        result = 0
        for s_el in s:
            while second < len(t):
                if t[second] != s_el:
                    second += 1
                else:
                    result += 1
                    break
        return result == 3


doctest.testmod()
