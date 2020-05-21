from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        row_num, col_num = len(grid), len(grid[0])
        queue = deque()
        hashset = set()
        res = 0
        def bfs(row, col):
            nonlocal hashset
            hashset.clear()
            hashset.add((row, col))
            queue.append((row, col))
            while len(queue) > 0:
                size = len(queue)
                for i in range(size):
                    r, c = queue.popleft()
                    if grid[r][c]=='0':
                        continue
                    grid[r][c] = '2'
                    if r > 0:
                        if (r - 1, c) not in hashset:
                            hashset.add((r - 1, c))
                            queue.append((r - 1, c))
                    if c > 0:
                        if (r, c - 1) not in hashset:
                            hashset.add((r, c - 1))
                            queue.append((r, c - 1))
                    if r < row_num - 1:
                        if (r + 1, c) not in hashset:
                            hashset.add((r + 1, c))
                            queue.append((r + 1, c))
                    if c < col_num - 1:
                        if (r, c + 1) not in hashset:
                            hashset.add((r, c + 1))
                            queue.append((r, c + 1))

        for row in range(row_num):
            for col in range(col_num):
                if grid[row][col] == '0' or grid[row][col] == '2':
                    continue
                else:
                    bfs(row, col)
                    res += 1
        return res


lst = [["1", "0", "0", "1", "1"],
       ["1", "0", "0", "0", "0"],
       ["0", "0", "1", "0", "0"],
       ["0", "0", "0", "1", "1"]]

s = Solution()
print(s.numIslands(lst))
