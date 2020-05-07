from collections import Counter
from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        lst = []
        res = []

        if root.val == x or root.val == y:
            return False

        def get_sub_tree(node: TreeNode, lev):
            val = node.val
            if val == x or val == y:
                res.append((lev, lst[-1]))
            lst.append(val)
            if node.left:
                get_sub_tree(node.left, lev + 1)
            if node.right:
                get_sub_tree(node.right, lev + 1)
            lst.pop()

        get_sub_tree(root, 0)
        if len(res) == 2 and res[0][0] == res[1][0] and res[0][1] != res[1][1]:
            return True
        else:
            return False


str1 = '[1,2,3,null,4]'
tree = stringToTreeNode(str1)
x = 2
y = 3
t1 = datetime.now()
s1 = Solution()
print(s1.isCousins(tree, x, y))
t2 = datetime.now()
print(t2 - t1)
