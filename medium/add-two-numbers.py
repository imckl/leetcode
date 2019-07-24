
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: list):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def to_int(node: ListNode):
            return node.val + 10 * to_int(node.next) if node else 0

        def to_list(n):
            node = ListNode(n % 10)
            if n >= 10:
                node.next = to_list(n / 10)
            return node

        return to_list(to_int(l1) + to_int(l2))



if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode([5, 6, 5])
    s = Solution()
    x = s.addTwoNumbers(l1, l2)
    print(x.val)
    pass