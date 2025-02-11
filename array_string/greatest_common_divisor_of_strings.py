"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only
if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

>>> Solution().gcdOfStrings("ABCABC", "ABC")
'ABC'

Example 2:

>>> Solution().gcdOfStrings("ABABAB", "ABAB")
'AB'

Example 3:

>>> Solution().gcdOfStrings("LEET", "CODE")
''

"""

import doctest


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(length: int) -> bool:
            if len1 % length or len2 % length:
                return False
            factor1, factor2 = len1 // length, len2 // length
            return str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2

        for gcd_length in range(min(len1, len2), 0, -1):
            if isDivisor(gcd_length):
                return str1[:gcd_length]
        return ""


doctest.testmod()
