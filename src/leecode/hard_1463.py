from datetime import datetime
from typing import List

'''
tag: ^1463 ^hard ^dp
name: ^(Cherry Pickup II)
'''


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * n for _ in range(n)] for _ in range(m)]

        for p1 in range(n):
            for p2 in range(n):
                dp[m - 1][p1][p2] = grid[m - 1][p1] if p1 == p2 else grid[m - 1][p1] + grid[m - 1][p2]

        for row in range(m - 2, -1, -1):
            for p1 in range(n):
                for p2 in range(n):
                    cur = grid[row][p1] if p1 == p2 else grid[row][p1] + grid[row][p2]
                    max_value = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            next_c1 = p1 + i
                            next_c2 = p2 + j
                            if -1 < next_c1 < n and -1 < next_c2 < n:
                                max_value = max(max_value, dp[row + 1][next_c1][next_c2])
                    dp[row][p1][p2] = cur + max_value

        return dp[0][0][-1]


grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
# grid = [[1, 0, 0, 0, 0, 0, 1],
#         [2, 0, 0, 0, 0, 3, 0],
#         [2, 0, 9, 0, 0, 0, 0],
#         [0, 3, 0, 5, 4, 0, 0],
#         [1, 0, 2, 3, 0, 0, 6]]

t1 = datetime.now()
s = Solution()
print(s.cherryPickup(grid))
t2 = datetime.now()
print(t2 - t1)
