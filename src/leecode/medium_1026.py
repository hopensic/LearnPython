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
    def maxAncestorDiff(self, root: TreeNode) -> int:
        lst = []
        dic = defaultdict(int)
        mx = 0
        def get_subtree(node: TreeNode):
            nonlocal mx
            if not node:
                return
            val = node.val
            if dic[val] == 0:
                dic[val] += 1
                if lst:
                    mx = max(mx, max([abs(i - val) for i in lst]))
                lst.append(val)
            if node.left:
                get_subtree(node.left)
            if node.right:
                get_subtree(node.right)
            lst.pop()
            dic[val] -= 1

        get_subtree(root)
        return mx


arr1 = '[8,3,10,1,6,null,14,null,null,4,7,13]'
tree = stringToTreeNode(arr1)
t1 = datetime.now()
s = Solution()
print(s.maxAncestorDiff(tree))
t2 = datetime.now()
print(t2 - t1)
