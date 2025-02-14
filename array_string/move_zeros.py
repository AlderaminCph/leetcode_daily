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

>>> Solution().moveZeroes([0,0,1])
[1, 0, 0]

"""

import doctest


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            print(nums)
            return

        i = 0  # index for non zero elements
        for j, element in enumerate(nums):
            if element:  # if the element is not zero
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        print(nums)


doctest.testmod()
