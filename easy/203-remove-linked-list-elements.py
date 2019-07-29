# 删除链表中等于给定值 val 的所有节点。
# https://leetcode-cn.com/problems/remove-linked-list-elements/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next

        if not head:
            return head

        node = head

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return head
