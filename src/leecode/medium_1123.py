from datetime import datetime
from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1123 ^medium ^tree ^dfs
name: ^(Lowest Common Ancestor of Deepest Leaves)
'''


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        res_node, level = self.get_sub(root, 0)
        return res_node

    def get_sub(self, node: TreeNode, level):
        if node.left is None and node.right is None:
            return node, level
        if node.left:
            left_node, left_level = self.get_sub(node.left, level + 1)
        else:
            left_node, left_level = None, level
        if node.right:
            right_node, right_level = self.get_sub(node.right, level + 1)
        else:
            right_node, right_level = None, level
        if left_level == right_level:
            return node, left_level
        elif left_level > right_level:
            return left_node, left_level
        else:
            return right_node, right_level


arr1 = '[1,2,3,4]'
node = stringToTreeNode(arr1)

t1 = datetime.now()
s = Solution()
print(s.lcaDeepestLeaves(node))
t2 = datetime.now()
print(t2 - t1)
