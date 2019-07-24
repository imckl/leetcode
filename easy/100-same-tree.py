
# https://leetcode-cn.com/problems/same-tree/
# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if (p and not q) or (not p and q):
            return False
        if not p or not q:
            return True
        if p.val != q.val:
            return False
        if (p.left and not q.left) or (p.right and not q.right):
            return False
        if p.left and q.left:
            return self.isSameTree2(p.left, q.left)
        if p.right and q.right:
            return self.isSameTree2(p.right, q.right)
        return False


if __name__ == '__main__':
    a = TreeNode(2)
    b = TreeNode(None)
    c = TreeNode(4)
    a.left = b
    a.right = c

    x = TreeNode(2)
    y = TreeNode(3)
    z = TreeNode(4)
    x.left = y
    x.right = z

    solution = Solution()
    r = solution.isSameTree(a, x)

    print(r)
