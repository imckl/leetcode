
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

from typing import List
import functools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return TreeNode(None)

        mid = len(nums) >> 1
        p_node = TreeNode(nums[mid])
        p_node.left = self.sortedArrayToBST(nums[:mid])
        p_node.right = self.sortedArrayToBST(nums[mid + 1:])

        return p_node

    def sortedArrayToBST3(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        mid = length >> 1

        i = 1
        root = TreeNode(nums[mid])
        tmp_tn = root

        while mid - i >= 0:
            tmp_tn.left = TreeNode(nums[mid - i])
            tmp_tn = tmp_tn.left
            i += 1

        i = 1
        tmp_tn = root
        while length - i > mid:
            tmp_tn.right = TreeNode(nums[length - i])
            tmp_tn = tmp_tn.left
            i += 1

        return root

    def _sortedArrayToBST(self, nums: List[int], tn: TreeNode) -> TreeNode:
        pass

    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        depth = 1
        n_max_node = lambda n: functools.reduce(lambda a, b: a + b, range(1, n + 1))

        while length > n_max_node(depth):
            depth += 1

        print(length, depth, n_max_node(depth))




if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    nums = [-10, -3, 0, 5, 9, 10, 11, 12, 13]
    solution = Solution()
    r = solution.sortedArrayToBST(nums)
    print(r)
