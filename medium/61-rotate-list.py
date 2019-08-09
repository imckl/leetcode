# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# https://leetcode-cn.com/problems/rotate-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return head

        # 链表长度
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        # print(length)

        # 可达到同样值的最小右移次数
        k %= length

        # 首尾相接
        node = head
        for _ in range(length - 1):
            node = node.next
        # print(node)
        # print(head)
        node.next = head

        # 移动至旋转中轴点
        node = head
        for _ in range(length - k):
            node = node.next
        new_head = node

        # 移动原链表长度次
        node = new_head
        for _ in range(length - 1):
            node = node.next

        # 截取链表
        node.next = None

        return new_head
