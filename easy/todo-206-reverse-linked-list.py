
# reverse-linked-list
# https://leetcode-cn.com/problems/reverse-linked-list/
# 反转一个单链表。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prev_node = None
        curr_node = head

        while curr_node:
            tmp_next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = tmp_next

        return prev_node


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    solution = Solution()
    result = solution.reverseList(head)
    print(result)


if __name__ == '__main__':
    main()
