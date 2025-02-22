"""
334. Increasing Triplet Subsequence

Given an integer array nums,
return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.


Example 1:

>>> Solution().increasingTriplet([1,2,3,4,5])
True

Explanation: Any triplet where i < j < k is valid.
Example 2:

>>> Solution().increasingTriplet([5,4,3,2,1])
False

Explanation: No triplet exists.
Example 3:

>>> Solution().increasingTriplet([2,1,5,0,4,6])
True

Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

>>> Solution().increasingTriplet([0,4,2,1,0,-1,-3])
False
"""

import doctest


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        inf = 2**31
        first, second = inf, inf
        for el in nums:
            if first >= el:
                first = el
            elif second >= el:
                second = el
            else:
                return True
        return False


doctest.testmod()
