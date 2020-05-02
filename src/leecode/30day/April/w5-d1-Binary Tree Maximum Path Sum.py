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
            left_value = max(0,get_sub_sum(subtree.left))
            right_value = max(0, get_sub_sum(subtree.right))
            max_value=max(max_value,left_value+right_value+subtree.val)
            return

            root_value = subtree.val
            if subtree.left:
                left_value = get_sub_sum(subtree.left)
                max_value = max(max_value, left_value)
            if subtree.right:
                right_value = get_sub_sum(subtree.right)
                max_value = max(max_value, right_value)

            if subtree.left and subtree.right:
                value_passed_root = max()
                tmp = max(root_value, root_value + left_value, root_value + right_value,
                          root_value + left_value + right_value)
                max_value = max(max_value, tmp)

                # 返回元组(经过root的值，不经过root的值)
                return()


                return tmp
            elif subtree.left and not subtree.right:
                tmp = max(root_value, left_value, root_value + left_value)
                max_value = max(max_value, tmp)
                return tmp
            elif not subtree.left and subtree.right:
                tmp = max(root_value, right_value, root_value + right_value)
                max_value = max(max_value, tmp)
                return tmp
            else:
                max_value = max(max_value, root_value)
                return root_value

        t = get_sub_sum(root)
        return max(max_value, t)


arr = '[5,4,8,11,null,13,4,7,2,null,null,null,1]'
# arr = '[1,-2,-3,1,3,-2,null,-1]'
tree = stringToTreeNode(arr)
t1 = datetime.now()
s = Solution()
print(s.maxPathSum(tree))
t2 = datetime.now()
print(t2 - t1)
