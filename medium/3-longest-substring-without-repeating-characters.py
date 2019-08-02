# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ln_result = ListNode(None)
        prev_node = ln_result
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev_node.next = ListNode(carry % 10)
            prev_node = prev_node.next
            carry //= 10

        return ln_result


class Solution2(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        int_result = self._get_all_node_val(l1) + self._get_all_node_val(l2)
        str_result = str(int_result)
        # print(int_result)

        ln_result = ListNode(int(str_result[-1]))
        tmp_node = ln_result
        for c in str_result[-2::-1]:
            tmp_node.next = ListNode(int(c))
            tmp_node = tmp_node.next

        return ln_result

    def _get_all_node_val(self, ln: ListNode) -> int:
        val = []
        tmp_node = ln
        while tmp_node:
            val.append(tmp_node.val)
            tmp_node = tmp_node.next
        val.reverse()
        val = int(''.join([str(i) for i in val]))
        return val
