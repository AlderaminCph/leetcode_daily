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
        lowercased_str = s.lower()
        vowels = ["a", "e", "i", "o", "u"]
        indexes_of_vowels = []
        for index, letter in enumerate(lowercased_str):
            if letter in vowels:
                indexes_of_vowels.append(index)
        retrieved_vowels = [s[i] for i in indexes_of_vowels]
        reverted_vowels = dict(
            [(index, letter) for (letter, index) in zip(retrieved_vowels[::-1], indexes_of_vowels)]
        )
        result = [s[i] if i not in indexes_of_vowels else reverted_vowels[i] for i in range(len(s))]
        return "".join(result)


doctest.testmod()
