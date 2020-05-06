from datetime import datetime
from typing import List

'''
tag: ^1043 ^medium ^graph ^dp
name: ^(Partition Array for Maximum Sum)
'''


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [[0] * (len(A) + 1) for _ in range(K + 1)]
        for i in range(1, K + 1):
            dp[i][1] = A[0]

        for i in range(2, len(A) + 1):
            dp[1][i] = A[i - 1] + dp[1][i - 1]

        for i in range(2, len(A) + 1):
            tmp = float('-inf')
            for j in range(1, K + 1):
                dp[j][i] = dp[K][i - j] + j * max(A[i - j:i]) if i - j >= 0 else i * max(A[:i])
                tmp = max(tmp, dp[j][i])
                dp[j][i] = tmp

        return dp[-1][-1]


A = [1, 15, 7, 9, 2, 5, 10]
K = 3

t1 = datetime.now()
s = Solution()
print(s.maxSumAfterPartitioning(A, K))
t2 = datetime.now()
print(t2 - t1)
