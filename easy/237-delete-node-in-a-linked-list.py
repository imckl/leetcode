# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


class Solution2(object):
    def deleteNode(self, node: ListNode) -> None:
        while node:
            if node.next and node.next.next:
                node.val = node.next.val
                node = node.next
            elif node.next:
                node.val = node.next.val
                node.next = None
            else:
                break
