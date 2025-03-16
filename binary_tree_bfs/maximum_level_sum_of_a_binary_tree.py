"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree,
the level of its root is 1,
the level of its children is 2, and so on.

Return the smallest level x such that the sum of all
the values of nodes at level x is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

"""

import sys
from collections import deque


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        queue = deque()
        queue.append(root)
        max_level_sum = -sys.maxsize
        level, max_level = 0, 0

        while queue:
            size = len(queue)
            current_sum = 0
            level += 1
            for _ in range(size):
                temp = queue.popleft()
                current_sum += temp.val
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if current_sum > max_level_sum:
                max_level_sum = current_sum
                max_level = level
        return max_level
