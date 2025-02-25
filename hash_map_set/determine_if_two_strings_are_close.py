"""
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain
one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into
another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2,
return true if word1 and word2 are close, and false otherwise.

Example 1:

>>> Solution().closeStrings(word1 = "abc", word2 = "bca")
True

Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

>>> Solution().closeStrings(word1 = "a", word2 = "aa")
False

Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

>>> Solution().closeStrings(word1 = "cabbba", word2 = "abbccc")
True

Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""

import doctest


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        word1_cnt = [word1.count(item) for item in set(word1)]
        word2_cnt = [word2.count(item) for item in set(word2)]
        word1_cnt.sort()
        word2_cnt.sort()
        if word1_cnt == word2_cnt:
            return True
        return False


doctest.testmod()
