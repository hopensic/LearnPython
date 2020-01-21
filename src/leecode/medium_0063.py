from datetime import datetime
from collections import Counter

'''
tag: ^0063 ^medium ^array ^dp
name: ^(Unique Paths II)
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1:
            return 0 if obstacleGrid[0].count(1) > 0 else 1
        if n == 1:
            return 0 if sum(obstacleGrid[i][0] for i in range(m)) > 0 else 1
        if obstacleGrid[0][0]==1:
            return 0
        if obstacleGrid[m-1][n-1]==1:
            return 0


        bottom_right = obstacleGrid[m - 1][n - 1]

        # 初始化最右列
        last_column = n - 1
        for i in range(m - 1, -1, -1):
            if obstacleGrid[i][last_column] == 0:
                obstacleGrid[i][last_column] = 1
            else:
                obstacleGrid[i][last_column] = -1
                break
        # 将剩余最后一列都改成0
        if i > 0:
            for j in range(i - 1, -1, -1):
                obstacleGrid[j][last_column] = -1

        # 初始化底行
        obstacleGrid[m - 1][n - 1] = bottom_right
        last_row = m - 1
        for i in range(n - 1, -1, -1):
            if obstacleGrid[last_row][i] == 0:
                obstacleGrid[last_row][i] = 1
            else:
                obstacleGrid[last_row][i] = -1
                break
        # 将剩余最后一行都改成0
        if i > 0:
            for j in range(i - 1, -1, -1):
                obstacleGrid[last_row][j] = -1

        # 将2改成1，将1改成0，遍历所有的grid
        for i in range(m - 1):
            for j in range(n - 1):
                obstacleGrid[i][j] = -1 if obstacleGrid[i][j] == 1 else obstacleGrid[i][j]

        for j in range(n - 2, -1, -1):
            for i in range(m - 2, -1, -1):
                if obstacleGrid[i][j] == -1:
                    continue
                bottom = 0 if obstacleGrid[i + 1][j] == -1 else obstacleGrid[i + 1][j]
                right = 0 if obstacleGrid[i][j + 1] == -1 else obstacleGrid[i][j + 1]
                obstacleGrid[i][j] = bottom + right
        return obstacleGrid[0][0]


# arr1 = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0]]
arr1 = [[0, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0]]
t1 = datetime.now()
s = Solution()
print(s.uniquePathsWithObstacles(arr1))
t2 = datetime.now()
print(t2 - t1)
