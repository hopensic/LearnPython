from collections import defaultdict
from datetime import datetime
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode

'''
tag: ^1457 ^medium ^bit-manipulation ^tree ^dfs
name: ^()
'''


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        lst, res = [0] * 10, 0

        def get_num_of_palindromic(node: TreeNode):
            nonlocal res
            # 是叶子节点
            lst[node.val] ^= 1
            if not node.left and not node.right:
                res += 1 if lst.count(1) < 2 else 0
            else:
                if node.left: get_num_of_palindromic(node.left)
                if node.right: get_num_of_palindromic(node.right)
            lst[node.val] ^= 1

        get_num_of_palindromic(root)
        return res


arr1 = '[2,1,1,1,3,null,null,null,null,null,1]'
root = stringToTreeNode(arr1)

t1 = datetime.now()
s = Solution()
print(s.pseudoPalindromicPaths(root))
t2 = datetime.now()
print(t2 - t1)
