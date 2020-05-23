from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1448 ^medium ^tree ^dfs
name: ^(Count Good Nodes in Binary Tree)
'''


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def getMax(node: TreeNode, mx=float('-inf')):
            nonlocal res
            if node.val >= mx:
                mx = node.val
                res += 1
            if node.left:
                getMax(node.left, mx)
            if node.right:
                getMax(node.right, mx)

        getMax(root)
        return res

    def goodNodes2(self, r, ma=-10000):
        return self.goodNodes2(r.left, max(ma, r.val)) + self.goodNodes2(r.right, max(ma, r.val)) + (
                r.val >= ma) if r else 0


arr1 = '[3,1,4,3,null,1,5]'
root = stringToTreeNode(arr1)

print((1 + 2 > 0) + 1)

t1 = datetime.now()
s = Solution()
print(s.goodNodes2(root))

t2 = datetime.now()
print(t2 - t1)
