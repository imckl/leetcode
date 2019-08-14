# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionNotMine:

    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        dummy = ListNode(None)
        dummy.next = head

        slow = dummy
        fast = dummy.next

        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp_val = fast.val
                # 在快指针上，跳过所有值重复的节点
                while fast and fast.val == tmp_val:
                    # 继续移动快指针
                    fast = fast.next
            else:
                # 慢指针 next 指向快指针 fast
                slow.next = fast
                # 当前慢指针设置为当前快指针
                slow = fast
                # 继续移动快指针
                fast = fast.next

        #
        slow.next = fast

        return dummy.next


# Runtime: 40 ms, faster than 97.68% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.9 MB, less than 8.00% of Python3 online submissions for Remove Duplicates from Sorted List II.
class Solution2:

    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        new_head = ListNode(None)
        new_node = new_head
        node = head

        # 用于标记状态：节点值是否重复
        same = False

        while node:

            # 如果有下一节点
            if node.next:
                # 如果当前节点值等于下一节点值，则标记为当前状态为节点值重复
                if node.val == node.next.val:
                    # 激活状态
                    same = True
                # 否则，如果当前状态为节点值重复
                elif same:
                    # 重置状态
                    same = False
                # 否则，当前节点不为重复值节点，添加至新链表中
                else:
                    new_node.next = node
                    new_node = new_node.next
            # 否则，检查当前状态是否为节点值重复；如果不是，啧添加至新链表中
            elif not same:
                new_node.next = node
                new_node = new_node.next

            node = node.next

        # 截断
        new_node.next = None

        # 返回
        return new_head.next
