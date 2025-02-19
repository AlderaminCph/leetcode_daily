"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

>>> Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
6

Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

>>> Solution().longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)
10

Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

>>> Solution().longestOnes(nums = [0,0,1,1,1,0,0], k = 0)
3

>>> Solution().longestOnes(nums = [0,0,0,1], k = 4)
4


"""

import doctest


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        Dynamic sliding window
        """
        left_bound_sliding_window = current_number_of_zeros_in_window = 0
        for el in nums:
            if el == 0:
                current_number_of_zeros_in_window += 1
            if current_number_of_zeros_in_window > k:
                if nums[left_bound_sliding_window] == 0:
                    current_number_of_zeros_in_window -= 1
                left_bound_sliding_window += 1  # move left bound to the right by one
        return len(nums) - left_bound_sliding_window


doctest.testmod()
