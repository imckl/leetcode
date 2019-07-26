
# 编写一个程序，找到两个单链表相交的起始节点。
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        tail_a, tail_b = headA, headB
        len_a, len_b = 1, 1

        # 行至链表A尾巴
        while True:
            if tail_a.next:
                tail_a = tail_a.next
                len_a += 1
            else:
                break

        # 行至链表B尾巴
        while True:
            if tail_b.next:
                tail_b = tail_b.next
                len_b += 1
            else:
                break

        # 如果链尾一致，则两链表相交
        # 然后，选取较长的链表，并移动至两链表长度差的位置
        # 此时，两链表长度一致，并且已知两链表相交
        # 那么，一次比较两链表的对应节点，节点一致则为相交节点
        if tail_a is tail_b:
            if len_a > len_b:
                head_long, head_short = headA, headB
            else:
                head_long, head_short = headB, headA

            for _ in range(abs(len_a - len_b)):
                head_long = head_long.next

            while head_long:
                if head_long == head_short:
                    return head_long
                head_long = head_long.next
                head_short = head_short.next
        else:
            return None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        node_a, node_b = headA, headB
        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else headA
        return node_a


if __name__ == '__main__':
    pass
