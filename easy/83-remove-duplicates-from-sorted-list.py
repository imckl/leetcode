
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        if head.next and head.val == head.next.val:
            head = head.next
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)

        return head
