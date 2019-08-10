
# 计算给定二叉树的所有左叶子之和。
# https://leetcode-cn.com/problems/sum-of-left-leaves/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self._sum = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self._dfs(root)
        return self._sum

    def _dfs(self, node: TreeNode):
        if not node:
            return

        if node.left and not node.left.left and not node.left.right:
            self._sum += node.left.val

        self._dfs(node.left)
        self._dfs(node.right)



class Solution2(object):
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
