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
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(
                reduce(
                    lambda x, y: x * y,
                    [el for j, el in enumerate(nums) if j != i],
                    1,
                )
            )
        return answer


doctest.testmod()
