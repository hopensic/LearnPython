from leecode.common.official import stringToTreeNode
from leecode.common.common_class import TreeNode
from datetime import datetime


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxlen = 0

        def get_level(r: TreeNode) -> int:
            nonlocal maxlen
            if not r: return 0
            # 左子树和右子树深度
            left_level, right_level = get_level(r.left), get_level(r.right)
            maxlen = max(left_level + right_level, maxlen)
            return max(left_level, right_level) + 1

        get_level(root)

        return maxlen


# arr = '[1,2,3,4,5]'
arr = '[1,2,3,4,5]'
t = stringToTreeNode(arr)
t1 = datetime.now()
s = Solution()
print(s.diameterOfBinaryTree(t))
t2 = datetime.now()
print(t2 - t1)
