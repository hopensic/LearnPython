# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        x, t = self.get_subtree(root)
        print('---')

    def get_subtree(self, node: TreeNode):
        if node is None:
            return 0, None

        t = TreeNode(node.val)
        left_num, left_subtree = self.get_subtree(node.left)
        right_num, right_subtree = self.get_subtree(node.right)

        if left_num > 0 or right_num > 0:
            if left_num > 0:
                t.left = left_subtree
            if right_num > 0:
                t.right = right_subtree
            return 1, t
        else:
            if t.val > 0:
                return 1, t
            else:
                return 0, None


# tree = '[0]'
tree = '[1,0,1,0,0,0,1]'
tree = '[1,1,0,1,1,0,1,0]'
root1 = stringToTreeNode(tree)

s = Solution()
s.pruneTree(root1)
print('----')
