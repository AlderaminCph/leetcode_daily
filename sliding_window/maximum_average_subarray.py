"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has
the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

>>> Solution().findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)
12.75

Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

>>> Solution().findMaxAverage(nums = [5], k = 1)
5.0

>>> Solution().findMaxAverage(nums = [4,0,4,3,3], k = 5)
2.8

>>> Solution().findMaxAverage(nums = [9,7,3,5,6,2,0,8,1,9], k = 6)
5.33333

"""

import doctest


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])  # current sum of sliding window of size k
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i]  # slide window across array
            current_sum -= nums[i - k]
            max_sum = max(max_sum, current_sum)

        if k == len(nums):
            max_sum = sum(nums)
        return round(max_sum / k, 5)


doctest.testmod()
