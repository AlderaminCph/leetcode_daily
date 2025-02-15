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
"""

import doctest


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 2):
            for j in range(1, len(nums) - 1):
                for k in range(2, len(nums)):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
        return False


doctest.testmod()
