from datetime import datetime
from collections import Counter

'''
tag: ^980 ^hard ^Backtracking ^dfs
name: ^(Unique Paths III)
'''

'''
使用回溯法，dfs
经过的地方设为3，回退以后设为0 

'''


class Solution:
    def uniquePathsIII(self, grid: list) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        total_zero = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total_zero += 1
                if grid[i][j] == 1:
                    start = (j, i)
                if grid[i][j] == 2:
                    end = (j, i)
        # 用于统计dfs时，经过的空格的数
        nums = 0
        # 用于存放路径的stack
        pos_stack = [start]
        # 代表每个格子的4个方向 (4: North; 3:East; 2:South; 1:West )
        direction_grid = [[4] * n for _ in range(m)]
        while len(pos_stack) > 0:
            curX, curY = pos_stack[-1]
            # 获取下一个位置的方向
            nextX, nextY = -1, -1

            while True > 0:
                cur_direction = direction_grid[curY][curX]
                if cur_direction == 4:
                    direction_grid[curY][curX] -= 1
                    nextX, nextY = curX, curY - 1
                    if nextY < 0:
                        continue
                    if grid[nextY][nextX] == 1 or grid[nextY][nextX] == -1:
                        continue
                    break
                elif cur_direction == 3:
                    direction_grid[curY][curX] -= 1
                    nextX, nextY = curX + 1, curY
                    if nextX == n:
                        continue
                    if grid[nextY][nextX] == 1 or grid[nextY][nextX] == -1:
                        continue
                    break

                elif cur_direction == 2:
                    direction_grid[curY][curX] -= 1
                    nextX, nextY = curX, curY + 1
                    if nextY == m:
                        continue
                    if grid[nextY][nextX] == 1 or grid[nextY][nextX] == -1:
                        continue
                    break
                elif cur_direction == 1:
                    direction_grid[curY][curX] -= 1
                    nextX, nextY = curX - 1, curY
                    if nextX < 0:
                        continue
                    if grid[nextY][nextX] == 1 or grid[nextY][nextX] == -1:
                        continue
                    break
                else:
                    direction_grid[curY][curX] = 4
                    grid[curY][curX] = 0
                    nums -= 1
                    # 将当前位置弹出栈
                    pos_stack.pop()
                    break

            # 如果4个方向都不对，将当前位置方向置为4
            if direction_grid[curY][curX] == 4:
                continue
            else:
                # 如果是break出来的，说明已经找到下一个位置
                # 如果找到出口
                if grid[nextY][nextX] == 2:
                    if nums == total_zero:
                        res += 1
                        direction_grid[curY][curX] = 4
                        grid[curY][curX] = 0
                        nums -= 1
                        pos_stack.pop()
                else:
                    grid[nextY][nextX] = 1
                    nums += 1
                    pos_stack.append((nextX, nextY))
        return res


arr1 = [[0,1],[2,0]]

t1 = datetime.now()
s = Solution()
print(s.uniquePathsIII(arr1))
t2 = datetime.now()
print(t2 - t1)
