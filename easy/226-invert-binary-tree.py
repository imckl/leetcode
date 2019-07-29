
# 翻转一棵二叉树。
# https://leetcode-cn.com/problems/invert-binary-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root


class Solution2(object):
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root
