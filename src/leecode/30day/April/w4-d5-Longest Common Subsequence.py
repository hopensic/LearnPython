from collections import defaultdict, Counter
from datetime import datetime
import bisect


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        le1, le2 = len(text1), len(text2)
        dp = [[0] * le2 for _ in range(le1)]
        if text1[0] == text2[0]:
            dp[0][0] = 1

        for j in range(1, le2):
            dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j - 1]
        for i in range(1, le1):
            dp[i][0] = 1 if text1[i] == text2[0] else dp[i - 1][0]

        for i in range(1, le1):
            for j in range(1, le2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[le1 - 1][le2 - 1]


text1 = "ab"
text2 = "b"

t1 = datetime.now()
s = Solution()
print(s.longestCommonSubsequence(text1, text2))
t2 = datetime.now()
print(t2 - t1)
