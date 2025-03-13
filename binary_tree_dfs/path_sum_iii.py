"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum,
return the number of paths where the sum of the values along
the path equals targetSum.

The path does not need to start or end at the root or a leaf,
but it must go downwards (i.e., traveling only from parent nodes to child nodes).


Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
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
        self.number_of_path = 0
        self.count_number_of_occurences_each_sum = {0: 1}

    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        if not root:
            return 0

        return self.dfs(node=root, current_running_sum=0, target_sum=targetSum)

    def dfs(
        self,
        node: TreeNode | None,
        current_running_sum: int,
        target_sum: int,
    ):
        if not node:  # we reached the last node
            return 0

        # add the current node value to the running sum
        current_running_sum += node.val

        # handle paths that start in the middle of the tree
        if (current_running_sum - target_sum) in self.count_number_of_occurences_each_sum:
            answer = self.count_number_of_occurences_each_sum[current_running_sum - target_sum]
        else:
            answer = 0
        if current_running_sum in self.count_number_of_occurences_each_sum:
            self.count_number_of_occurences_each_sum[current_running_sum] += 1
        else:
            self.count_number_of_occurences_each_sum[current_running_sum] = 1

        if node.left:
            answer += self.dfs(node.left, current_running_sum, target_sum)
        if node.right:
            answer += self.dfs(node.right, current_running_sum, target_sum)

        # decrement the prefix sum count
        if current_running_sum in self.count_number_of_occurences_each_sum:
            self.count_number_of_occurences_each_sum[current_running_sum] -= 1
        else:
            self.count_number_of_occurences_each_sum[current_running_sum] = 0

        return answer
