"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good
if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

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
    def __init__(self):
        self.cnt = 0

    def goodNodes(self, root: TreeNode) -> int:
        max_value = -(10**5)

        self.dfs(root, max_value)

        return self.cnt

    def dfs(self, root: TreeNode, max_val: int):
        if not root:
            return
        if root.val >= max_val:
            self.cnt += 1
            max_val = root.val
        self.dfs(root.left, max_val)
        self.dfs(root.right, max_val)
