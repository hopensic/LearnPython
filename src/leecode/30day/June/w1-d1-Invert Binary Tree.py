from collections import Counter
from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        if not root.left and not root.right:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# str1 = '[1,2,3,null,4,5,6]'
# str1 = '[4,2,7,1,3,6,9]'
str1 = '[4]'
tree = stringToTreeNode(str1)
t1 = datetime.now()
s1 = Solution()
print(s1.invertTree(tree))
t2 = datetime.now()
print(t2 - t1)
