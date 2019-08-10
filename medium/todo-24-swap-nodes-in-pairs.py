
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(None)
        dummy.next = head

        node = dummy

        node = head
        while node:
            node = self._swapPairs(node)
        return head

    def _swapPairs(self, node: ListNode) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = node

        # 如果节点有下一位
        if node.next:
            # 获得原第一个节点
            former_first_node = node
            # 获得原第二个节点
            former_second_node = node.next
            # 获得原第二节点的下一节点（原第三个节点）
            former_third_node = node.next.next
            # 交换原第一、第二个节点
            node = former_second_node
            node.next = former_first_node
            # 让新的第二个节点指向原第三个节点
            node.next.next = former_third_node

            return node.next.next
        # 如果节点没有下一位
        else:
            return None