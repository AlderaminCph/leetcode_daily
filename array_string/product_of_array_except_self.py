"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[i].

The product of any prefix or suffix of nums is guaranteed to
fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time
and without using the division operation.

Example 1:

>>> Solution().productExceptSelf([1,2,3,4])
[24, 12, 8, 6]

Example 2:

>>> Solution().productExceptSelf([-1,1,0,-3,3])
[0, 0, 9, 0, 0]
"""

import doctest


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        suffix_product = [1] * (len(nums))
        prefix_product = [1] * (len(nums))
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        answer = [prefix_product[i] * suffix_product[i] for i in range(len(nums))]
        return answer


doctest.testmod()
