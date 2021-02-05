from datetime import datetime
from typing import List

'''
tag: ^1572 ^easy ^array
name: ^(Matrix Diagonal Sum)
'''


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        le = len(mat)
        if le == 1:
            return mat[0][0]
        res = 0
        t = le // 2
        for i in range(t):
            p = -(i + 1)
            res += (mat[i][i] + mat[i][p] + mat[p][i] + mat[p][p])
        if le % 2 == 1:
            res += mat[t][t]
        return res


mat = [[7, 3, 1, 9],
       [3, 4, 6, 9],
       [6, 9, 6, 6],
       [9, 5, 8, 5]]

t1 = datetime.now()
s = Solution()
print(s.diagonalSum(mat))
t2 = datetime.now()
print(t2 - t1)
