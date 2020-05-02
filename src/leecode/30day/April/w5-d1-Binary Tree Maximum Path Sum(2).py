from datetime import datetime
from leecode.common.official import stringToTreeNode

from leecode.common.common_class import TreeNode


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        max_value = -99999999

        def get_sub_sum(subtree: TreeNode):
            nonlocal max_value
            if not subtree:
                return 0
            left_value = max(0, get_sub_sum(subtree.left))
            right_value = max(0, get_sub_sum(subtree.right))
            max_value = max(max_value, left_value + right_value + subtree.val)
            return max(left_value, right_value) + subtree.val

        get_sub_sum(root)
        return max_value


arr = '[5,4,8,11,null,13,4,7,2,null,null,null,1]'
# arr = '[1,-2,-3,1,3,-2,null,-1]'
tree = stringToTreeNode(arr)
t1 = datetime.now()
s = Solution()
print(s.maxPathSum(tree))
t2 = datetime.now()
print(t2 - t1)
