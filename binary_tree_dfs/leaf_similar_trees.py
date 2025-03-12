"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order,
the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

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
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        first_tree_end_nodes, second_tree_end_nodes = [], []

        self.dfs(root1, first_tree_end_nodes)
        self.dfs(root2, second_tree_end_nodes)
        return first_tree_end_nodes == second_tree_end_nodes

    def dfs(self, root: TreeNode | None, nodes: list):
        if root.left:
            self.dfs(root.left, nodes)
        if root.right:
            self.dfs(root.right, nodes)
        if root.left == root.right:
            nodes.append(root.val)
