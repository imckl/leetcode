
# https://leetcode-cn.com/problems/path-sum/
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 说明: 叶子节点是指没有子节点的节点。

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        sum_ = 0
        return self._has_path_sum(root, require_sum=sum, sum_=sum_)

    def _has_path_sum(self, root: TreeNode, require_sum: int, sum_: int) -> bool:
        if not root:
            return False
        sum_ += root.val
        if not root.left and not root.right:
            if require_sum == sum_:
                return True
        return self._has_path_sum(root.left, require_sum, sum_) or self._has_path_sum(root.right, require_sum, sum_)


if __name__ == '__main__':
    groot = TreeNode(1)

    groot.left = TreeNode(2)
    groot.right = TreeNode(3)

    groot.left.left = TreeNode(4)
    groot.left.right = TreeNode(5)
    groot.right.left = TreeNode(6)
    groot.right.right = TreeNode(7)

    groot.left.left.left = TreeNode(8)
    groot.left.left.right = TreeNode(9)
    groot.left.right.left = TreeNode(10)
    groot.left.right.right = TreeNode(11)
    groot.right.left.left = TreeNode(12)
    groot.right.left.right = TreeNode(13)
    groot.right.right.left = TreeNode(14)
    groot.right.right.right = TreeNode(15)

    s = Solution()
    print(s.hasPathSum(groot, 23, 0))