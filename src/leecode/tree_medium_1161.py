from collections import defaultdict

import numpy as np

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        dic = defaultdict(int)
        dic[level] = root.val

        def cal_sum(node: TreeNode, lev: int):
            if node:
                dic[lev + 1] += node.val
                cal_sum(node.left, lev + 1)
                cal_sum(node.right, lev + 1)

        cal_sum(root.left, level)
        cal_sum(root.right, level)

        ret = 0
        val = np.iinfo(np.int).min
        # for index, v in enumerate(list(accumulate(dic.values(), add))):
        for k, v in dic.items():
            if v > val:
                val = v
                ret = k
        return ret


string = ' [1,7,0,7,-8,null,null]'
# string = '[989,null,10250,98693,-89388,null,null,null,-32127]'
node = stringToTreeNode(string)

s = Solution()
print(s.maxLevelSum(node))
