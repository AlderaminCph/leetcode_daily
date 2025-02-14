"""
283. Move Zeroes

Given an integer array nums,
move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

>>> Solution().moveZeroes([0,1,0,3,12])
[1, 3, 12, 0, 0]

Example 2:

>>> Solution().moveZeroes([0])
[0]

"""

import doctest


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            i += 1
        return nums


doctest.testmod()
