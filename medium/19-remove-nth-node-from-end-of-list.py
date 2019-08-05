# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        none_node = ListNode(None)
        fast = head
        slow = none_node
        slow.next = head
        # 要移除倒数第 n 个节点 ->
        # 将倒数第 n + 1 个节点链接到倒数第 n - 1 个节点上 ->
        # 找到倒数第 n - 1 个节点 - >
        # 延迟 n - 1 + 1 步再移动慢指针
        remain_count = n - 1 + 1

        while fast:

            fast = fast.next

            if remain_count <= 0:
                slow = slow.next

            remain_count -= 1

        if slow == none_node:
            head = head.next
        else:
            slow.next = slow.next.next if slow.next.next else None

        return head


class Solution3:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        fast = head
        slow = head
        # 要移除倒数第 n 个节点 ->
        # 将倒数第 n + 1 个节点链接到倒数第 n - 1 个节点上 ->
        # 找到倒数第 n - 1 个节点 - >
        # 延迟 n - 1 + 1 步再移动慢指针
        remain_count = n - 1 + 1

        while fast:

            fast = fast.next

            if remain_count <= 0:
                slow = slow.next

            remain_count -= 1

        if head == slow:
            return head.next

        node = head
        while node:
            if node.next == slow:
                node.next = node.next.next if node.next.next else None
                break
            node = node.next

        return head


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head:
            return head

        nodes = []
        node = head

        while node:
            nodes.append(node)
            node = node.next

        length = len(nodes)
        if n == length:
            return head.next

        nodes[-n - 1].next = nodes[-n - 1].next.next
        return head
