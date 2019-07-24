
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right,
# level by level from leaf to root).

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        # 第一行
        result = [[root.val]]
        n = 1

        self._dfs(root, n, result)

        return result

    def _dfs(self, tn: TreeNode, n: int, result: List[List[int]]):
        if len(result) < n + 1:
            if tn.left or tn.right:
                result.insert(0, [])

        if tn.left:
            result[len(result) - n - 1].append(tn.left.val)
            self._dfs(tn.left, n + 1, result)
        if tn.right:
            result[len(result) - n - 1].append(tn.right.val)
            self._dfs(tn.right, n + 1, result)


class Solution2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        self._dfs(root, result, 1)
        return result

    def _dfs(self, tn: TreeNode, result: List[List[int]], n: int):
        if tn:
            if len(result) < n + 1:
                result.insert(0, [])
            result.append(tn.val)
            self._dfs(tn.left, result, n + 1)
            self._dfs(tn.right, result, n + 1)