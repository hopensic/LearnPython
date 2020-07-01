from typing import List
from bisect import bisect_left, insort

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        lst = [1, 1]
        for i in range(2, n + 1):
            temp = 0
            x = (i + 1) // 2 - 1
            for j in range(x):
                temp += lst[j] * lst[i - 1 - j] * 2
            temp += lst[x] * lst[i - 1 - x] * (2 if i % 2 == 0 else 1)
            lst.append(temp)

        return lst[n]


n = 2
# nums = '[1,2,3,4,5,6]'
# nums = '[1, 1, 1, 2, 0, 1, 99]'
# tree = stringToTreeNode(nums)
# 1,1; 2,2; 7,429;
so = Solution()
print(so.numTrees(n))
