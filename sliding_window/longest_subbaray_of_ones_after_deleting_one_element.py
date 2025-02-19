"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's
in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1]
longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

>>> Solution().longestSubarray(nums = [1,1,1])
2

Explanation: You must delete one element.

"""

import doctest


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1

        max_length, current_length = 0, 0
        for el in nums:
            if el == 1:
                current_length += 1
            elif el == 0 and (current_length + 1 > max_length):
                current_length += 1
                max_length = current_length
                current_length = 0
            max_length = max(current_length, max_length)
        return max_length


doctest.testmod()
