from typing import List
from bisect import bisect_left, insort

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        return 0 if not root \
            else 1 + self.countNodes(root.left) + self.countNodes(root.right)


# nums = '[1,2,3,4,5,6]'
nums = '[1, 1, 1, 2, 0, 1, 99]'
tree = stringToTreeNode(nums)

so = Solution()
print(so.countNodes(tree))
