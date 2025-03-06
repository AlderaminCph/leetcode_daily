"""
206. Reverse Linked List

Given the head of a singly linked list,
reverse the list, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

"""

import doctest


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        prev_node, next_node = head, head.next

        while next_node and next_node.next:
            next_node.next = prev_node
            prev_node = prev_node.next
            next_node = prev_node.next

        return next_node


doctest.testmod()
