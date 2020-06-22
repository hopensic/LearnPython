from functools import reduce
from typing import List
from bisect import bisect_left, insort

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        lst = list(range(1, n + 1))
        t = 0
        stacks = []

        def get_num():
            nonlocal t
            if len(lst) == 0:
                t += 1
                if t == k:
                    print(stacks)
                    return True
            for i in lst:
                stacks.append(i)
                lst.remove(i)
                if get_num():
                    return True
            insort(lst, stacks.pop())

        get_num()
        return "".join([str(c) for c in stacks])


n = 4
k = 9
so = Solution()
so.getPermutation(n, k)
