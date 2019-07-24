
# https://blog.csdn.net/cocoiehl/article/details/80959143
# https://www.cnblogs.com/anzhengyu/p/11083568.html


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 前序遍历(中左右)
    @staticmethod
    def dfs_preorder(root: TreeNode):
        print('前序遍历(中左右)', 'dfs_preorder', '迭代')
        if not root:
            return

        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                print(node.val)
                stack.append(node.right)
                stack.append(node.left)

    # 中序遍历(左中右)
    @staticmethod
    def dfs_inorder(root: TreeNode):
        print('中序遍历(左中右)', 'dfs_inorder', '迭代')
        if not root:
            return

        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            print(root.val)
            root = root.right

    # 后序遍历(左右中)
    @staticmethod
    def dfs_postorder(root: TreeNode):
        print('后序遍历(左右中)', 'dfs_postorder', '迭代')
        if not root:
            return

        stack = []

        while stack or root:
            while root:
                stack.append(root)
                if root.left:
                    root = root.left
                else:
                    root = root.right
            s = stack.pop()
            print(s.val)

            # 如果当前节点是上一节点的左子节点，则遍历右子节点
            if stack and s == stack[-1].left:
                root = stack[-1].right
            else:
                root = None

    # 层次遍历
    @staticmethod
    def bfs(root: TreeNode):
        print('层次遍历(bfs)', '迭代')
        queue = [root]
        while queue:
            n = len(queue)
            print('n', n)
            for i in range(n):
                q = queue.pop(0)
                if q:
                    print(q.val)
                    queue.append(q.left if q.left is not None else None)
                    queue.append(q.right if q.right is not None else None)

    # 后序遍历(左右中)
    def dfs_postorder_recursive(self, root: TreeNode):
        # print('后序遍历(左右中)', 'dfs_postorder', '递归')
        if not root:
            return
        self.dfs_postorder_recursive(root.left)
        self.dfs_postorder_recursive(root.right)
        print(root.val)

    # 前序遍历(中左右)
    def dfs_preorder_recursive(self, root: TreeNode):
        # print('前序遍历(中左右)', 'dfs_preorder', '迭代')
        if not root:
            return
        print(root.val)
        self.dfs_preorder_recursive(root.left)
        self.dfs_preorder_recursive(root.right)

    # 中序遍历(左中右)
    def dfs_inorder_recursive(self, root: TreeNode):
        if not root:
            return
        self.dfs_inorder_recursive(root.left)
        print(root.val)
        self.dfs_inorder_recursive(root.right)

    # 根节点到叶子节点的所有路径。
    def traverse(self, node: TreeNode):
        if not node.left and not node.right:
            return [str(node.val)]
        left, right = [], []
        if node.left:
            left = [str(node.val) + x for x in self.traverse(node.left)]
        if node.right:
            right = [str(node.val) + x for x in self.traverse(node.right)]

        return left + right


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

    solution = Solution()
    # r = solution.minDepth(root)
    # print(r)
    # r = solution.bfs(root)
    # r = solution.dfs_preorder(root)
    # r = solution.dfs_inorder(root)
    # r = solution.dfs_postorder(root)
    # r = solution.dfs_postorder_recursive(root)
    # solution.dfs_inorder_recursive(groot)
    print(solution.traverse(groot))
