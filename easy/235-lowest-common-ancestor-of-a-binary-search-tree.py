
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        lowest_common_node = root

        while lowest_common_node:
            if lowest_common_node.val > max_val:
                lowest_common_node = lowest_common_node.left
            elif lowest_common_node.val < min_val:
                lowest_common_node = lowest_common_node.right
            else:
                return lowest_common_node
