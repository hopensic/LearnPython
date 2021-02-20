from datetime import datetime
from typing import List

'''
tag: ^1605 ^medium ^greedy
name: ^(Find Valid Matrix Given Row and Column Sums)
'''


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        res = [[0] * n for _ in range(m)]
        i, j = 0, 0

        while i < m and j < n:
            if rowSum[i] < colSum[j]:
                res[i][j] = rowSum[i]
                colSum[j] -= res[i][j]
                i += 1
            else:
                res[i][j] = colSum[j]
                rowSum[i] -= res[i][j]
                j += 1

        return res


rowSum = [5, 7, 10]
colSum = [8, 6, 8]

t1 = datetime.now()
s = Solution()
print(s.restoreMatrix(rowSum, colSum))
t2 = datetime.now()
print(t2 - t1)
