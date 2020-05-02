from datetime import datetime

'''
tag: ^1130 ^medium ^dp ^stack ^tree
name: ^(Minimum Cost Tree From Leaf Values)
'''


class Solution:
    def mctFromLeafValues(self, arr: list) -> int:
        maxvalue = 2 ** 31
        le = len(arr)
        dp = [[0] * le for _ in range(le)]
        for i in range(le - 1):
            dp[i][i + 1] = arr[i] * arr[i + 1]
        if le == 2:
            return dp[0][1]
        def get_i_j(i: int, j: int):
            if i == j:
                return 0
            if dp[i][j] == 0:
                tmp = maxvalue
                for k in range(i, j):
                    dp[i][k] = get_i_j(i, k)
                    dp[k + 1][j] = get_i_j(k + 1, j)
                    tmp = min(tmp, dp[i][k] + dp[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j + 1]))
                dp[i][j] = tmp
                return tmp
            else:
                return dp[i][j]

        return get_i_j(0, le - 1)


arr1 = [7,3,8,5,4,9]

t1 = datetime.now()
s = Solution()
print(s.mctFromLeafValues(arr1))
t2 = datetime.now()
print(t2 - t1)
