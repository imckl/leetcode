
# https://leetcode-cn.com/problems/symmetric-tree/
# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        p = root.left
        q = root.right
        return self._isSymmetric(p, q)

    def _isSymmetric(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self._isSymmetric(p.left, q.right) and self._isSymmetric(p.right, q.left)


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True


if __name__ == '__main__':
    pass