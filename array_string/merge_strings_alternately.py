"""
1768. Merge Strings Alternately

You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

>>> Solution().merge_alternately("abc", "pqr")
'apbqcr'

Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

>>> Solution().merge_alternately("ab", "pqrs")
'apbqrs'

Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

>>> Solution().merge_alternately("abcd", "pq")
'apbqcd'

Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""

import doctest


class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        first_ptr, second_ptr = 0, 0
        merged_word = []
        while first_ptr < len(word1) and second_ptr < len(word2):
            merged_word.extend([word1[first_ptr], word2[second_ptr]])
            first_ptr += 1
            second_ptr += 1
        if first_ptr < len(word1):
            merged_word.extend(word1[first_ptr:])
        if second_ptr < len(word2):
            merged_word.extend(word2[second_ptr:])
        return "".join(merged_word)


doctest.testmod()
