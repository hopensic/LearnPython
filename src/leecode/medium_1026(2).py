from collections import defaultdict
from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1026 ^medium ^tree ^dfs
name: ^(Maximum Difference Between Node and Ancestor)
'''


class Solution:
    def maxAncestorDiff(self, root, mn=100000, mx=0):
        return max(self.maxAncestorDiff(root.left, min(mn, root.val), max(mx, root.val)),
                   self.maxAncestorDiff(root.right, min(mn, root.val), max(mx, root.val))) \
            if root else mx - mn


arr1 = '[8,3,10,1,6,null,14,null,null,4,7,13]'
tree = stringToTreeNode(arr1)
t1 = datetime.now()
s = Solution()
print(s.maxAncestorDiff(tree))
t2 = datetime.now()
print(t2 - t1)
