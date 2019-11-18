# Definition for a binary tree node.
from leecode.common.commons import buildTree, TreeNode

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

    def traverse(self, node, num, parent=None):
        if node:
            print(node.val)
        else:
            return 0
        right_sum = 0
        left_sum = 0
        if (node.right):
            right_sum = self.traverse(node.right, 1)
        d[node.val] = node.val + right_sum
        if (node.left):
            left_sum = self.traverse(node.left, 0, d[node.val])
        if (num == 1):
            d[node.val] = node.val + right_sum
        else:
            d[node.val] = node.val + parent + right_sum
        return node.val + right_sum + left_sum


treelist = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
root_tree = buildTree(treelist)
print('-----')

solution = Solution()
# solution.bstToGst(root_tree)
solution.traverse(root_tree, 1)
