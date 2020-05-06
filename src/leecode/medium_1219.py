from datetime import datetime
from typing import List

'''
tag: ^1219 ^medium ^backtracking
name: ^(Path with Maximum Gold)
'''


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        mx = 0
        m, n = len(grid), len(grid[0])

        def dfs(row, col, cur_val):
            nonlocal mx
            if grid[row][col] <= 0:
                return 0
            grid[row][col] *= -1
            # 四个方向走
            up, left, down, right = 0, 0, 0, 0
            if row > 0:
                up = dfs(row - 1, col, - grid[row][col])
            if col > 0:
                left = dfs(row, col - 1, - grid[row][col])
            if row < m - 1:
                down = dfs(row + 1, col, - grid[row][col])
            if col < n - 1:
                right = dfs(row, col + 1, - grid[row][col])

            # 复原
            grid[row][col] *= -1
            return grid[row][col] + max(up, left, down, right)

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    mx = max(mx, dfs(i, j, grid[i][j]))

        return mx


grid = [[1, 0, 7],
        [2, 0, 6],
        [3, 4, 5],
        [0, 3, 0],
        [9, 0, 20]]

t1 = datetime.now()
s = Solution()
print(s.getMaximumGold(grid))
t2 = datetime.now()
print(t2 - t1)
