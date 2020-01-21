from datetime import datetime
from collections import Counter

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1302 ^medium ^tree ^dfs
name: ^(Deepest Leaves Sum)
'''


class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        sums, _ = self.get_sum(root, 1)
        return sums

    def get_sum(self, node: TreeNode, dept: int):
        left_sum, right_sum = 0, 0

        if node.left is None and node.right is None:
            return (node.val, dept)
        else:
            dep_left, dep_right = 0, 0
            if node.left:
                left_sum, dep_left = self.get_sum(node.left, dept + 1)
            if node.right:
                right_sum, dep_right = self.get_sum(node.right, dept + 1)
            if dep_left > dep_right:
                return (left_sum, dep_left)
            elif dep_left < dep_right:
                return (right_sum, dep_right)
            else:
                return (left_sum + right_sum, dep_left)


node = '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
root = stringToTreeNode(node)

t1 = datetime.now()
s = Solution()
print(s.deepestLeavesSum(root))
t2 = datetime.now()
print(t2 - t1)
