# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。

from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        return self._binaryTreePaths(root)

    def _binaryTreePaths(self, node: TreeNode) -> List[str]:
        if not node.left and not node.right:
            return [str(node.val)]

        left, right = [], []

        if node.left:
            left = [str(node.val) + '->' + s for s in self._binaryTreePaths(node.left)]
        if node.right:
            right = [str(node.val) + '->' + s for s in self._binaryTreePaths(node.right)]

        return left + right
