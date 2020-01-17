import operator
from collections import defaultdict
from datetime import datetime
from itertools import accumulate

'''
tag: ^1074 ^hard ^array ^dp ^sliding window
name: ^(Number of Submatrices That Sum to Target)
'''


class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        num = 0
        M, N = len(matrix), len(matrix[0])

        for lst in matrix:
            for i, x in enumerate(accumulate(lst, operator.add)):
                lst[i] = x

        for j in range(N):
            for i, x in enumerate(accumulate([matrix[i][j] for i in range(M)], operator.add)):
                matrix[i][j] = x

        num += self.get_num(matrix[0], target)

        if M > 1:
            for i in range(1, M):
                for j in range(0, i):
                    num += self.get_num([matrix[i][t] - matrix[j][t] for t in range(N)], target)
                num += self.get_num(matrix[i], target)

        return num

    def get_num(self, lst: list, target: int):
        ret_num = 0
        dic = defaultdict(int)
        for prefix_sum in lst:
            tmp = prefix_sum - target
            ret_num = ret_num + 1 if prefix_sum == target else ret_num
            ret_num = ret_num + dic[tmp] if tmp in dic else ret_num
            dic[prefix_sum] += 1
        return ret_num


arr1 = [[1, 1, 0, 1, -1, 0, 1, 0, -1, 0, 0, 1],
        [-1, 1, 0, -1, -1, 0, 1, 0, -1, 0, 0, -1],
        [1, 1, 0, 1, -1, 0, -1, 0, -1, 0, 0, 1]]

target1 = 0

t1 = datetime.now()
s = Solution()
print(s.numSubmatrixSumTarget(arr1, target1))
t2 = datetime.now()
print(t2 - t1)
