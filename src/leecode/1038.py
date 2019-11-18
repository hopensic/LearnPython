# Definition for a binary tree node.
from leecode.common.commons import TreeNode, buildTree

d = {}


class Solution:

    def get_sumof_right(self, node):
        if (node):
            d[node.val] = node.val + self.get_sumof_right(node.right)
            return d[node.val] + self.get_sumof_left(node.left, d[node.val])
        else:
            return 0

    def get_sumof_left(self, node, parent):
        if (node):
            d[node.val] = node.val + self.get_sumof_right(node.right) + parent
            return node.val + self.get_sumof_left(node.left, d[node.val]) + self.get_sumof_right(node.right)
        else:
            return 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        sumof_right = self.get_sumof_right(root)
        d[root.val] = sumof_right
        root.val += sumof_right
        root.left.val += sumof_right + self.get_sumof_right(root.left.right)
        return root


treelist = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
# treelist = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
root_tree = buildTree(treelist)
print('-----')

solution = Solution()
solution.bstToGst(root_tree)

# print(solution.rangeSumBST(root_tree, 7, 15))
