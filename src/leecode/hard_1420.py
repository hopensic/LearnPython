from datetime import datetime

'''
tag: ^1420 ^hard ^dp
name: ^(Build Array Where You Can Find The Maximum Exactly K Comparisons)
'''


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 1000000007
        res = [[[0] * (k + 1) for i in range(m + 1)] for j in range(n + 1)]

        for j in range(1, m + 1):
            res[1][j][1] = 1

        for a in range(1, n + 1):
            for b in range(1, m + 1):
                for c in range(1, k + 1):
                    temp = 0
                    temp = (temp + b * res[a - 1][b][c]) % mod
                    for d in range(1, b):
                        temp = (temp + res[a - 1][d][c - 1]) % mod
                    res[a][b][c] = (res[a][b][c] + temp) % mod
        ret = 0
        for i in range(1, m + 1):
            ret = (ret + res[n][i][k]) % mod

        return ret


n = 37
m = 17
k = 7

t1 = datetime.now()
s = Solution()
print(s.numOfArrays(n, m, k))
t2 = datetime.now()
print(t2 - t1)
