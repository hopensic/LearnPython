from typing import List
from bisect import bisect_left, insort

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        def get_sum(node: TreeNode, parent_val=0):
            nonlocal res
            val = parent_val * 10 + node.val
            if not node.left and not node.right:
                res += val
            else:
                if node.left:
                    get_sum(node.left, val)
                if node.right:
                    get_sum(node.right, val)

        get_sum(root)
        return res


# nums = '[4,9,0,5,1]'
nums = '[1,2,3]'
tree = stringToTreeNode(nums)

so = Solution()
print(so.sumNumbers(tree))
