from collections import Counter
from datetime import datetime
from typing import List

from leecode.common.common_class import ListNode
from leecode.common.official import stringToListNode

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        costs.sort(key=lambda item: item[0] - item[1], reverse=True)
        le = len(costs)
        half = int(le / 2)
        for i in range(half):
            res += costs[i][1] + costs[i + half][0]
        return res


costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
t1 = datetime.now()
s1 = Solution()
print(s1.twoCitySchedCost(costs))
t2 = datetime.now()
print(t2 - t1)
