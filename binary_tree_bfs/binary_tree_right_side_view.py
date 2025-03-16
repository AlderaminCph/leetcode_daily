"""
199. Binary Tree Right Side View

Given the root of a binary tree,
imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []

"""


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        right_side_view_elements = []
        self.helper_function(root, right_side_view_elements, 0)
        return right_side_view_elements

    def helper_function(
        self, root: TreeNode, right_side_view_elements: list[int], current_level: int
    ):
        if not root:
            return
        if current_level == len(right_side_view_elements):
            # we reached a new level in the tree
            right_side_view_elements.append(root.val)
        self.helper_function(root.right, right_side_view_elements, current_level + 1)
        self.helper_function(root.left, right_side_view_elements, current_level + 1)
