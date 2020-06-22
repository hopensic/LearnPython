from functools import reduce
from typing import List
from bisect import bisect_left, insort

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dungeon[-1][-1] = 1 if 1 - dungeon[-1][-1] <= 0 else 1 - dungeon[-1][-1]
        for i in range(m - 2, -1, -1):
            t = dungeon[i + 1][n - 1] - dungeon[i][n - 1]
            dungeon[i][n - 1] = 1 if t <= 0 else t
        for i in range(n - 2, -1, -1):
            t = dungeon[m - 1][i + 1] - dungeon[m - 1][i]
            dungeon[m - 1][i] = 1 if t <= 0 else t

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                a = dungeon[i + 1][j] - dungeon[i][j]
                b = dungeon[i][j + 1] - dungeon[i][j]
                dungeon[i][j] = min(1 if a <= 0 else a, 1 if b <= 0 else b)
        return dungeon[0][0]


# dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
dungeon = [[-2, -3, 3]]
so = Solution()
print(so.calculateMinimumHP(dungeon))
