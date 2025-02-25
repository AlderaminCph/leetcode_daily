"""
1207. Unique Number of Occurrences

Given an array of integers arr,
return true if the number of occurrences of each value in the array is unique or false otherwise.



Example 1:

>>> Solution().uniqueOccurrences(arr = [1,2,2,1,1,3])
True

Explanation: The value 1 has 3 occurrences,
2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

>>> Solution().uniqueOccurrences(arr = [1,2])
False

Example 3:

>>> Solution().uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])
True

"""

import doctest


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurences = [arr.count(item) for item in arr]
        return len(set(occurences)) == len(set(arr))


doctest.testmod()
