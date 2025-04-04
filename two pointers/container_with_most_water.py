"""
11. Container With Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

>>> Solution().maxArea([1,8,6,2,5,4,8,3,7])
49

Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container
can contain is 49.

Example 2:

>>> Solution().maxArea([1,1])
1

>>> Solution().maxArea([8,7,2,1])
7
"""

import doctest


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        amount = 0

        while left < right:
            current_amount = min(height[left], height[right]) * (right - left)
            if current_amount > amount:
                amount = current_amount
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return amount


doctest.testmod()
