
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        n = 1
        p, q = root.left, root.right
        return self._walk_to_max_depth(p, q, n)

    def _walk_to_max_depth(self, p: TreeNode, q:TreeNode, n: int) -> int:
        if not p and not q:
            return n
        if not p:
            return self._walk_to_max_depth(q.left, q.right, n + 1)
        elif not q:
            return self._walk_to_max_depth(p.left, p.right, n + 1)
        else:
            return max(self._walk_to_max_depth(q.left, q.right, n + 1), self._walk_to_max_depth(p.left, p.right, n + 1))

    def max_depth_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1