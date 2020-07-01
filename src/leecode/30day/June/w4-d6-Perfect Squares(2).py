from typing import List
from bisect import bisect_left

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        dic ={i:i**2 for i in range(1, 511) }
        res = 0
        idx = bisect_left(lst, n)
        if lst[idx]==n:
            return 1


        print(idx)

        for i in range(2, n + 1):
            idx = bisect_left(lst, i)
            if lst[idx] == i:
                res.append(1)
                continue
            mn = float('inf')
            for j in range(idx):
                mn = min(mn, 1 + res[i - lst[j]])
            res.append(mn)
        return res[n]


n = 223842
so = Solution()
print(so.numSquares(n))
