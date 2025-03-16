"""
1372. Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node;
    otherwise, move to the left child.
    Change the direction from right to left or from left to right.
    Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1.
(A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Definition for a binary tree node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        return max(self.maxZigZag(root.left, True, 0), self.maxZigZag(root.right, False, 0))

    def maxZigZag(self, node: TreeNode, direction_left: bool, depth) -> int:
        if not node:
            return depth

        if direction_left:
            depth = max(
                depth,
                self.maxZigZag(node.right, False, depth + 1),
                self.maxZigZag(node.left, True, 0),
            )
        else:
            depth = max(
                depth,
                self.maxZigZag(node.left, True, depth + 1),
                self.maxZigZag(node.right, False, 0),
            )

        return depth
