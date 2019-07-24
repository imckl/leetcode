
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/balanced-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._not_balanced = -1      # value indicating not balanced(since height won't be -1)

    def isBalanced(self, root: TreeNode) -> bool:
        height = self._get_height(root)
        return height != self._not_balanced

    def _get_height(self, node: TreeNode) -> int:
        if not node:
            return 0

        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)

        if left_height == self._not_balanced or right_height == self._not_balanced:
            return self._not_balanced
        if abs(left_height - right_height) > 1:
            return self._not_balanced
        return max(left_height, right_height) + 1


class Solution5:
    def __init__(self):
        self.is_balanced = True

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self._get_height(root)
        return self.is_balanced

    def _get_height(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        if abs(left_height - right_height) > 1:
            self.is_balanced = False

        return max(left_height, right_height) + 1


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def _get_height(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        return max(left_height, right_height) + 1


class Solution4:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_depth, right_depth = 0, 0
        if root.left:
            left_depth = self._get_depth(root.left)
        if root.right:
            right_depth = self._get_depth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def _get_depth(self, root: TreeNode):
        if not root:
            return 0
        return max(self._get_depth(root.left), self._get_depth(root.right)) + 1


class Solution3:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        height = self._get_height_and_check_is_balanced(root)
        print(height)
        return height != False

    def _get_height_and_check_is_balanced(self, root: TreeNode):
        if not root:
            return 0
        left_height = self._get_height_and_check_is_balanced(root.left)
        right_height = self._get_height_and_check_is_balanced(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return max(left_height, right_height) + 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution = Solution()
    solution.isBalanced(root)
    pass
