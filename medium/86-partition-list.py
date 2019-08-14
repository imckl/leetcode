# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
# https://leetcode.com/problems/partition-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        if not head:
            return head

        dummy_left_head = ListNode(None)
        dummy_right_head = ListNode(None)

        node = head

        dummy_left = dummy_left_head
        dummy_right = dummy_right_head

        while node:

            if node.val < x:
                dummy_left.next = node
                dummy_left = node
            else:
                dummy_right.next = node
                dummy_right = node

            node = node.next

        dummy_left.next = dummy_right_head.next
        dummy_right.next = None

        return dummy_left_head.next
