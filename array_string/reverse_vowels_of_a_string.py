"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', a
nd they can appear in both lower and upper cases, more than once.

Example 1:

>>> Solution().reverseVowels("IceCreAm")
'AceCreIm'

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

>>> Solution().reverseVowels("leetcode")
'leotcede'


"""

import doctest


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        resulted_string = list(s)
        while i < j:
            while i < j and resulted_string[i] not in vowels:
                i += 1
            while i < j and resulted_string[j] not in vowels:
                j -= 1
            if i < j:
                resulted_string[i], resulted_string[j] = resulted_string[j], resulted_string[i]
                i, j = i + 1, j - 1
        return "".join(resulted_string)


doctest.testmod()
