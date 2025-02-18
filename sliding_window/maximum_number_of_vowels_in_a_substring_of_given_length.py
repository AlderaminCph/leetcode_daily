"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of
vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

>>> Solution().maxVowels(s = "abciiidef", k = 3)
3

Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

>>> Solution().maxVowels(s = "aeiou", k = 2)
2

Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

>>> Solution().maxVowels(s = "leetcode", k = 3)
2

Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

import doctest


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        current_vowels_number = sum([s[:k].count(vowel) for vowel in vowels])
        max_value = current_vowels_number

        for i in range(k, len(s)):
            current_vowels_number += int(s[i] in vowels) - int(s[i - k] in vowels)
            max_value = max(max_value, current_vowels_number)

        if k == len(s):
            max_value = sum([s.count(vowel) for vowel in vowels])

        return max_value


doctest.testmod()
