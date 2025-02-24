"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's
in the resulting array. Return 0 if there is no such subarray.



Example 1:

>>> Solution().longestSubarray(nums = [1,1,0,1])
3

Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

>>> Solution().longestSubarray(nums = [0,1,1,1,0,1,1,0,1])
5

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
        left, right = 0, 0
        answer = 0
        number_of_zeros_in_subarray = 0
        for right, el in enumerate(nums):
            if el == 0:
                number_of_zeros_in_subarray += 1
            while number_of_zeros_in_subarray > 1:
                number_of_zeros_in_subarray -= nums[left] ^ 1
                left += 1
            answer = max(answer, right - left)
        return answer


doctest.testmod()
